from gogettr import PublicClient

client = PublicClient()


def test_user_posts():
    """Verifies we can extract posts for a simple, known user."""
    posts = list(client.user_activity(username="support", max=5, type="posts"))
    assert len(posts) > 0


def test_user_posts_max():
    """Verifies that we pull at most `max` posts."""
    posts = list(client.user_activity(username="dailynews", max=21, type="posts"))
    assert len(posts) == 21


def test_user_comments():
    """Verifies we can extract comments for a simple, known user."""
    comments = list(
        client.user_activity(username="dineshdsouza", max=5, type="comments")
    )
    assert len(comments) > 0


def test_user_likes():
    """Verifies we can extract comments for a simple, known user."""
    comments = list(client.user_activity(username="support", max=10, type="likes"))
    assert len(comments) == 10


def test_user_pagination():
    """Verifies we can extract paginated activity for a simple, known user."""
    activity = list(
        client.user_activity(username="dineshdsouza", max=40, type="comments")
    )
    assert len(activity) == 40
