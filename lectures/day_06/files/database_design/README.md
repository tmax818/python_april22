# Database Design

- **Do not repeat data**
- normalization means reduced repetition
- identifiers  and  foreign keys = glue between tables
- each table needs to be good at one thing: storing instances of the data
- we create tables based on the task in question
- we want to save storage space

## Tyler's Tips:

- ONE table for ONE real world object or relationship
- a column is ONE piece of info about the object
- decide before hand how the tables are related(i.e. one-to-many or many-to-many)
- try to reduce redundant data (normalize)