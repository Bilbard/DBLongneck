# DBLongneck

A dead simple database for Python 3. Now with compression!

A fancy way of formatting JSON files with memory consumption in mind. 

Intended as an easy alternative to SQL-like databases in small projects for those who do not want to deal with SQL.

# Usage

Import the file as such, and initialize a database.

You can also pass debug=True to enable debug printing of every step the library takes.

```python
from dblongneck import Longneck

db = Longneck("desired/path/for/db")
```

Then you can do the following:

# Update(Directory (STRING), Data (DICT))

The directory here is relative to the directory given when you initialized the database. 

```python
from dblongneck import Longneck

db = Longneck("desired/path/for/db")

db.Update("foo", {"foo":"bar"})

db.Update("os/best", {"windows":7})

db.Update("foo", {"obamna":"SODA!!!"})
```

This example will create foo.dbl in the root of the database, and best.dbl in root/os, like so:

```json
{
    "dbl": "DBLongneckFile",
    "dbld": "11/12/2022-22:59:35",
    "ver": "1.0",
    "windows": 7
}

{
    "dbl": "DBLongneckFile",
    "dbld": "11/12/2022-23:00:35",
    "ver": "1.0",
    "foo": "bar",
    "obamna": "SODA!!!"
}
```

# Check(Diectory (STRING))

Intended for internal use, but can be used to verify a file/directory. If this fails to find either, it will create them.

```python
from dblongneck import Longneck

db = Longneck("desired/path/for/db")

db.Check("foo")

db.Check("os/best")
```

This would check that the examples from the previous command are present. If it creates any new files, it populates them with a default header containing an identifier, the date of creation, and a version number.

# Load(Directory (STRING))

Also for internal use, but allows you to load a file as DBL sees it.

```python
from dblongneck import Longneck

db = Longneck("desired/path/for/db")

dosomething = db.Load("foo")
```

Returns the dictionary saved in the file. This also runs a Check, so it (should) always at least return the default header.

# Wipe(Directory (STRING), Delete=False (Bool))

Simply wipes the given file. Resets to default state with header, date and version.

```python
from dblongneck import Longneck

db = Longneck("desired/path/for/db")

db.Wipe("foo")
```

Should you pass True to delete, it will instead simply delete the file. The size of a blank dbl is negligible, but some clean freaks will like this method better.
