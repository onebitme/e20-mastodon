from mastodon import Mastodon

'''
Mastodon.create_app(
     'pytooterapp',
     api_base_url = 'https://hehe',
     to_file = 'pytooter_clientcred.secret'
)
'''

# Then login. This can be done every time, or use persisted.

from mastodon import Mastodon

mastodon = Mastodon(client_id = 'pytooter_clientcred.secret')
mastodon.log_in(
    'my_login_email@example.com',
    'incrediblygoodpassword',
    to_file = 'pytooter_usercred.secret'
)

# To post, create an actual API instance.

from mastodon import Mastodon

mastodon = Mastodon(access_token = 'pytooter_usercred.secret')
mastodon.toot('Tooting from Python using #mastodonpy !')