# GoGettr
GoGettr is an extraction tool for GETTR, a "non-bias [sic] social network." (We will not reward their domain with a hyperlink.)

This tool does not currently require any authentication with GETTR; it gathers all its data through publicly accessible endpoints.

Currently, this tool can:

* Pull all the posts made on the platform
* Pull all the posts of a user on the platform

## Robustness

This tool was made by "reverse engineering" GETTR's API. (It wasn't that hard.) Because we have no insight into GETTR's internals, there's no guarantee that this tool provides an exhaustive or reliable export of GETTR content. Still, it does a pretty good job.

## CLI Playbook

#### Pull all posts (starting at id 1)

```
gogettr all-posts
```

#### Pull all posts (starting at a particular ID and moving backward through IDs)

```
gogettr all-posts --rev --last pay8d
```

#### Pull all posts from a user

```
gogettr user USERNAME --type posts
```

#### Pull all comments from a user

```
gogettr user USERNAME --type comments
```

#### Pull all likes from a user

```
gogettr user USERNAME --type likes
```

#### Pull a user's information

```
gogettr user-info USERNAME
```

## CLI Usage

```
Usage: gogettr [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  all-posts  Pull all posts sequentially.
  user       Pull the posts, likes, or comments made by a user.
  user-info  Pull given user's information.
```

### `all-posts`

```
Usage: gogettr all-posts [OPTIONS]

  Pull all posts sequentially.

Options:
  --first TEXT   the ID of the first post to pull
  --last TEXT    the ID of the last post to pull
  --max INTEGER  the maximum number of posts to pull
  --rev          increment reverse chronologically (i.e., from last to first)
  --help         Show this message and exit.
```

### `user`

```
Usage: gogettr user [OPTIONS] USERNAME

  Pull the posts, likes, or comments made by a user.

Options:
  --max INTEGER                  the maximum number of activities to pull
  --until TEXT                   the ID of the earliest activity to pull for
                                 the user
  --type [posts|comments|likes]
  --help                         Show this message and exit.
```

### `user-info`

```
Usage: gogettr user-info [OPTIONS] USERNAME

  Pull given user's information.

Options:
  --help  Show this message and exit.
```

## Module Usage

You can use GoGettr as a Python module. For example, here's how you would pull all a user's posts:

```python
from gogettr import PublicClient
client = PublicClient()
posts = client.user_activity(username="support", type="posts")
```

For more examples of using GoGettr as a module, check out the [tests directory](tests/).

## Development

To run gogettr in a development environment, you'll need [Poetry](https://python-poetry.org). Install the dependencies by running `poetry install`, and then you're all set to work on gogettr locally.

To run the tests, run `poetry run pytest`.

To access the CLI, run `poetry run gogettr`.

## Wishlist

We hope to add support for the following capabilities to GoGettr:

- [ ] Pull a user's followers
- [ ] Pull who a user is following
- [ ] Pull trends
- [ ] Pull suggested users
- [ ] Pull all comments for a post
- [ ] Pull all comments on the platform
- [ ] Pull all users on the platform
- [ ] Search for content
- [ ] Multithreaded/concurrent API requests for sequential scans (e.g., pulling all posts on the platform)
