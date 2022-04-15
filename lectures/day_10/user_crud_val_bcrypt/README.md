# user CRUD with basic Validation

## Validation methods will be static methods on our models

```py
    @staticmethod
    def validate_user(user):
        is_valid = True # we assume this is true
        if len(user['first_name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(user['last_name']) < 3:
            flash("Last name must be at least 3 characters.")
            is_valid = False
        return is_valid
```

## We use the `validate_user` static method on form data

