from .api import APIClient
import os
from galeria.models import NASAImage
from typing import List, Dict, Union
from datetime import datetime, timedelta, date

class ImageAPI(APIClient):
    def __init__(self):
        super().__init__(baseUrl = "https://api.nasa.gov")
            
        
    def fetch(self, start_date, end_date) -> dict:
        date_range = self._get_date_range(start_date, end_date)
        
        if not self._is_saved(date_range):
            data = self.send_request(
                endpoint="/planetary/apod",
                params={
                    "thumbs": True,
                    "api_key": os.getenv('NASA_API'),
                    "start_date": start_date,
                    "end_date": end_date
                }
            )

            if data:
                self._save_to_db(data)    
    
    
    
    def _is_saved(self, dates: list) -> bool:
        
        existing_dates = NASAImage.objects.filter(date__in=dates).values_list('date', flat=True)
        converted_dates = {datetime.strptime(date, '%Y-%m-%d').date() for date in dates}
        
        return set(converted_dates) == set(existing_dates)
    
    
    def _save_to_db(self, data: List[Dict]) -> None:
        images = []
        for item in data:
            image_data = NASAImage(
                date=item.get("date"),
                title=item.get("title"),
                explanation=item.get("explanation"),
                url=item.get("thumbnail_url") if item.get("media_type") == "video" else item.get("url"),
                hdurl=item.get("url") if item.get("media_type") == "video" else item.get("hdurl"),
                media_type=item.get("media_type"),
                descricao=f"api.nasa.gov/{item.get('copyright', '')[1:] if item.get('copyright') else 'NASA'}",
                service_version=item.get("service_version")
            )
            images.append(image_data)
        
        if images:
            NASAImage.objects.bulk_create(images, ignore_conflicts=True)
            

    def _get_from_db(self, dates: List[str]) -> List[Dict]:
        images = NASAImage.objects.filter(date__in=dates)
        return images
    
    
    def _get_date_range(self, start_date: Union[str, date], end_date: Union[str, date]) -> List[str]:
        if isinstance(start_date, str):
            start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        if isinstance(end_date, str):
            end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

        date_range = [(start_date + timedelta(days=i)).isoformat() for i in range((end_date - start_date).days + 1)]
        
        return date_range
            
