import os, sys

start = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <title>Users</title>
</head>
<body>
"""

def make_form(table_name, action, route, params):
    filename = f"./templates_temp/{action}_{table_name}.html"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'a') as f:
        f.write(start)
        f.write(f'<form action="/{table_name}/{route}" method="post" class="col-6 mx-auto">\n')
        f.write(f'<h2 class="text-center">Edit {{{table_name}.{params[1]}}}</h2>\n')
        for item in params:
            f.write('        <div class="form-group">\n')
            f.write(f'            <label for="{item}">{item}</label>\n')
            f.write(f'            <input type="text" name="{item}" class="form-control">\n')
            f.write('        </div>\n')
        f.write(f'        <input type="submit" value="Submit" class="btn btn-success">')
        f.write("    </form>\n</body>\n</html>")

def make_index(table_name, route, params):
    filename = f"./templates_temp/{table_name}_index.html"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'a') as f:
        f.write(start)
        f.write("""
        <h1 class="text-center">Index</h1>
            <table class="table table-hover">
        <thead>
            <tr>
        """)
        for param in params:
            f.write(f'<th>{param}</th>')
            if param == params[-1]:
                f.write("</tr>\n</thead>\n<tbody>\n")
            else:
                f.write("\n")
        f.write(f"{{% for {table_name} in {table_name}s %}}\n")
        f.write("<td>\n")
        for param in params:
            f.write(f"<td>{{ {table_name}.{param} }}</td>")
            if param == params[-1]:
                f.write("</tr>\n{% endfor %}\n<tbody>\n</table>\n")
            else:
                f.write("\n")

def make_show(table_name, params):
    filename = f"./templates_temp/{table_name}_show.html"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'a') as f:
        f.write(f"""
        <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
        <title>User</title>
    </head>
    <body>
        <h2 class="text-center">{{{table_name.capitalize()} {{{table_name}.id}}}}</h2>
        """)
        for param in params:
            f.write(f"    <p>{param.capitalize()}: {{{table_name}.{param}}}</p>\n")
        f.write(f"""        
        <p>Created ON: {{{table_name}.created_at.strftime("%b %d %Y")}}</p>
        <p>Last Updated: {{{table_name}.updated_at.strftime("%b %d %Y")}}</p>
    </body>
    </html>
        """)



make_form(sys.argv[1], "new", "create", sys.argv[2:])
make_form(sys.argv[1], "edit", "update", sys.argv[2:])
make_index(sys.argv[1], "index", sys.argv[2:])
make_show(sys.argv[1], sys.argv[2:])

