import json
from datetime import datetime
from typing import Any, Dict, Type

class DateTimeJavaScriptConverter:
    def deserialize(self, data: Dict[str, Any], type_: Type) -> Any:
        if type_ is datetime:
            date_str = data.get('date')
            if date_str:
                return datetime.fromisoformat(date_str)
        return None

    def serialize(self, obj: Any) -> Dict[str, str]:
        if isinstance(obj, datetime):
            return {'date': obj.isoformat()}
        return {}

    @property
    def supported_types(self) -> Type:
        return datetime

# Usage example
converter = DateTimeJavaScriptConverter()

# Serialize a datetime object to a JSON-compatible format
dt = datetime.utcnow()
serialized = converter.serialize(dt)
print('Serialized:', json.dumps(serialized))

# Deserialize a JSON-compatible format back to a datetime object
data = {'date': dt.isoformat()}
deserialized = converter.deserialize(data, datetime)
print('Deserialized:', deserialized)
