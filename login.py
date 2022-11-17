# Then login. This can be done every time, or use persisted.

from mastodon import Mastodon

mastodon = Mastodon(client_id = 'pytooter_clientcred.secret')
mastodon.log_in(
    'my_login_email@example.com',
    'incrediblygoodpassword',
    to_file = 'pytooter_usercred.secret'
)