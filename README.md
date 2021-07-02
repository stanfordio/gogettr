# GoGettr
GoGettr is an extraction tool for GETTR, a "non-bias [sic] social network." (We will not reward their domain with a hyperlink.)

This tool does not currently require any authentication with GETTR; it gathers all its data through publicly accessible endpoints.

Currently, this tool can:

* Pull all the posts made on the platform
* Pull all the posts of a user on the platform

## Robustness

This tool was made by reverse engineering GETTR's API. (To be fair, it wasn't that hard.) Because we have no insight into GETTR's internals, there's no guarantee that this tool provides an exhaustive or reliable export of GETTR content. Still, it does a pretty good job.

## CLI Playbook

TODO

## CLI Usage

TODO

## Module Usage

You can use GoGettr as a Python module. For example, here's how you would pull all a user's posts:

```python
from gogettr import PublicClient
client = PublicClient()
posts = client.user_posts(username="support")
```

For more examples of using GoGettr as a module, check out the [tests directory](tests/).

# Wishlist

We hope to add support for the following capabilities to GoGettr:

- [ ] Pull a user's comments
- [ ] Pull a user's info
- [ ] Pull a user's likes
- [ ] Pull a user's followers
- [ ] Pull who a user is following
- [ ] Pull all comments for a post
- [ ] Pull all comments on the platform
- [ ] Pull all users on the platform
- [ ] Pull trends
- [ ] Pull suggested users
- [ ] Multithreaded/concurrent API requests for sequential scans (e.g., pulling all posts on the platform)