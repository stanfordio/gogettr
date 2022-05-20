# GoGettr

GoGettr is an API client for GETTR, a "non-bias [sic] social network." GoGettr is built and maintained by the [Stanford Internet Observatory](https://io.stanford.edu).

This tool does not currently require any authentication with GETTR; it gathers all its data through publicly accessible endpoints.

Currently, this tool can:

* Pull posts made on the platform
* Pull comments made on the platform
* Pull all top "trending" hashtags
* Pull all suggested users
* Pull all "trending" posts (i.e., the posts on the home page)
* Pull all posts and/or comments of a user on the platform
* Pull all a user's followers
* Pull all users a particular user follows
* Pull all comments on a particular post
* Pull profile information about particular users

GoGettr is designed for academic research, open source intelligence gathering, and data archival. It pulls all of the data from the publicly accessible API.

## Installation

GoGettr is available on PyPI. To install it, simply run `pip install gogettr`. Provided your `pip` is setup correctly, this will make `gogettr` available both as a command and as a Python package. **Note that GoGettr requires Python 3.8 or higher.**

## CLI Playbook

**Pull all posts (starting at id 1, capped at 1m)**

```bash
gogettr all --max 1000000
```

**Pull all comments**

```bash
gogettr all --type comments --max 1000000
```

**Pull all posts (starting at a particular ID and moving backward through IDs)**

```bash
gogettr all --rev --last pay8d
```

**Pull all posts from a user**

```bash
gogettr user USERNAME --type posts
```

**Pull all comments from a user**

```bash
gogettr user USERNAME --type comments
```

**Pull all likes from a user**

```bash
gogettr user USERNAME --type likes
```

**Pull a user's information**

```bash
gogettr user-info USERNAME
```

## CLI Usage

```text
Usage: gogettr [OPTIONS] COMMAND [ARGS]...

  GoGettr is an unauthenticated API client for GETTR.

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  all             Pull all posts (or comments) sequentially.
  comments        Pull comments on a specific post.
  hashtags        Pull the suggested hashtags (the top suggestions are...
  live            Pull livestream posts.
  search          Search posts for the given query.
  suggested       Pull the suggested users (users displayed on the home...
  trends          Pull all the trends (posts displayed on the home page).
  user            Pull the posts, likes, or comments made by a user.
  user-followers  Pull all a user's followers.
  user-following  Pull all users a given user follows.
  user-info       Pull given user's information.
```

### `all`

```text
Usage: gogettr all [OPTIONS]

  Pull all posts (or comments) sequentially.

  Note that if iterating chronologically and both max and last are unset, then
  this command will run forever (as it will iterate through all post IDs to
  infinity). To prevent this, either specify a max, last post, or iterate
  reverse chronologically.

  Posts will be pulled in parallel according to the desired number of workers.
  Out of respect for GETTR's servers, avoid setting the number of workers to
  values over 50.

Options:
  --first TEXT             the ID of the first post to pull
  --last TEXT              the ID of the last post to pull
  --max INTEGER            the maximum number of posts to pull
  --rev                    increment reverse chronologically (i.e., from last
                           to first)
  --type [posts|comments]
  --workers INTEGER        the number of threads to run in parallel
  --help                   Show this message and exit.
```

### `comments`

```text
Usage: gogettr comments [OPTIONS] POST_ID

  Pull comments on a specific post.

Options:
  --max INTEGER  the maximum number of comments to pull
  --help         Show this message and exit.
```

### `hashtags`

```text
Usage: gogettr hashtags [OPTIONS]

  Pull the suggested hashtags (the top suggestions are displayed on the front
  page).

  Note that while the first five or so hashtags have expanded information
  associated with them, later results do not.

Options:
  --max INTEGER  the maximum number of hashtags to pull
  --help         Show this message and exit.
```

### `search`

```text
Usage: gogettr search [OPTIONS] QUERY

  Search posts for the given query.

  This is equivalent to putting the query in the GETTR search box and
  archiving all the posts that result.

Options:
  --max INTEGER  the maximum number of posts to pull
  --help         Show this message and exit
```

### `suggested`

```text
Usage: gogettr suggested [OPTIONS]

  Pull the suggested users (users displayed on the home page).

Options:
  --max INTEGER  the maximum number of users to pull
  --help         Show this message and exit.
```

### `trends`

```text
Usage: gogettr trends [OPTIONS]

  Pull all the trends (posts displayed on the home page).

Options:
  --max INTEGER  the maximum number of posts to pull
  --until TEXT   the ID of the earliest post to pull
  --help         Show this message and exit.
```

### `user`

```text
Usage: gogettr user [OPTIONS] USERNAME

  Pull the posts, likes, or comments made by a user.

Options:
  --max INTEGER                  the maximum number of activities to pull
  --until TEXT                   the ID of the earliest activity to pull for
                                 the user
  --type [posts|comments|likes]
  --help                         Show this message and exit.
```

### `user-followers`

```text
Usage: gogettr user-followers [OPTIONS] USERNAME

  Pull all a user's followers.

Options:
  --max INTEGER  the maximum number of users to pull
  --help         Show this message and exit.
```

### `user-following`

```text
Usage: gogettr user-following [OPTIONS] USERNAME

  Pull all users a given user follows.

Options:
  --max INTEGER  the maximum number of users to pull
  --help         Show this message and exit.
```

### `user-info`

```text
Usage: gogettr user-info [OPTIONS] USERNAME

  Pull given user's information.

Options:
  --help  Show this message and exit.
```

### `live`

```text
Usage: gogettr live [OPTIONS]

  Pull livestream posts.

Options:
  --max INTEGER  the maximum number of livestream entries to pull
  --help         Show this message and exit.
```

## Module Usage

You can use GoGettr as a Python module. For example, here's how you would pull all a user's posts:

```python
from gogettr import PublicClient
client = PublicClient()
posts = client.user_activity(username="support", type="posts")
```

For more examples of using GoGettr as a module, check out the [tests directory](tests/). Note that the API surface can't be considered quite stable yet. In the case that Gettr changes their API, GoGettr's API may change to match (though with as few public-facing API changes as possible, however).

GoGettr groups related API functionality into the same capabilities; for example, pulling users' comments, posts, and likes is all done by the same function (inside `user_activity.py`), and pulling followers and following is done by the same function (inside `user_relationships.py`). That means there isn't perfect correspondence between the CLI surface and the API surface.

## Development

To run gogettr in a development environment, you'll need [Poetry](https://python-poetry.org). Install the dependencies by running `poetry install`, and then you're all set to work on gogettr locally.

To run the tests, run `poetry run pytest`.

To access the CLI, run `poetry run gogettr`.

To package and release a new version on PyPI, simply create a new release tag on GitHub.

## Contributing

Contributions are encouraged! For small bug fixes and minor improvements, feel free to just open a PR. For larger changes, please open an issue first so that other contributors can discuss your plan, avoid duplicated work, and ensure it aligns with the goals of the project. Be sure to also follow the [code of conduct](CODE_OF_CONDUCT.md). Thanks!

## Logging

When run in CLI mode, GoGettr will log extensive debug information to `gogettr.log` (in the working directory). This log will include every single request GoGettr makes, and every single response GoGettr receives. Because it's possible that GoGettr accidentally loses some information when parsing API responses, consider keeping this file around just in case.

## Wishlist

Support for the following capabilities is planned:

- ...nothing right now! (Got an idea? Submit an issue/PR!)
