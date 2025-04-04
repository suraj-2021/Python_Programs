class HybridRouter:
    
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'auth':
            return 'auth_db'
        if model._meta.app_label == 'analytics':
            return 'analytics_db'
        return 'replica'
    
    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'auth':
            return 'auth_db'
        if model._meta.app_label == 'analytics':
            return 'analytics_db'
        return 'primary'
    
    def allow_relation(self, obj1, obj2, **hints):
        # Allow relations between objects in the same database
        if obj1._state.db == obj2._state.db:
            return True
        
        # Special case: allow relations between primary and replica
        if {obj1._state.db, obj2._state.db} == {'primary', 'replica'}:
            return True
            
        return None
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'auth':
            return db == 'auth_db'
        if app_label == 'analytics':
            return db == 'analytics_db'
        if db in ['auth_db', 'analytics_db']:
            return False
        return None
