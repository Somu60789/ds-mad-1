from models import db, Service

def create_service(name, price, description, time_required):
    """Create a new service and save it to the database."""
    new_service = Service(name=name, price=price, description=description, time_required=time_required)
    db.session.add(new_service)
    db.session.commit()
    return new_service

def update_service(service_id, name=None, price=None, description=None, time_required=None):
    """Update an existing service by its ID."""
    service = Service.query.get(service_id)
    if service:
        if name:
            service.name = name
        if price is not None:
            service.price = price
        if description:
            service.description = description
        if time_required:
            service.time_required = time_required
        db.session.commit()
        return service
    return None

def delete_service(service_id):
    """Delete a service by its ID."""
    service = Service.query.get(service_id)
    if service:
        db.session.delete(service)
        db.session.commit()
        return True
    return False

def get_all_services():
    """Retrieve all services from the database."""
    return Service.query.all()

def get_service_by_id(service_id):
    """Retrieve a service by its ID."""
    return Service.query.get(service_id)
