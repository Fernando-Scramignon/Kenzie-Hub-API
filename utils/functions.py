def client_login(client, login_data, login_url):
    login_response = client.post(login_url, login_data)
    token = login_response.data['access']

    client.credentials(
        HTTP_AUTHORIZATION='Bearer ' + token
    )