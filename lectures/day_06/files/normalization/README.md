# Normalization

## What is Normalization?

>Database normalization is simply a convention for splitting large tables of data into smaller separate tables with the primary goal being to not repeat data.

# **It is possible to take normalization to an extreme.**

## The three forms:

### First Form

- one column, one value
![](../../../images/one-to-one.png)

### Second Form

- each column should have a unique value
  - except for keys

### Third Form

- no column should depend on another
  - except for keys
  - This is the form that you can take too far!!!!