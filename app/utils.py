from bson import ObjectId

def serialize_doc(doc):
    """Converts a MongoDB document to a JSON-serializable dictionary."""
    if doc is None:
        return None
    # Convert ObjectId to string
    doc['_id'] = str(doc['_id'])
    # Handle any nested ObjectIds (if applicable)
    for key, value in doc.items():
        if isinstance(value, ObjectId):
            doc[key] = str(value)
    return doc