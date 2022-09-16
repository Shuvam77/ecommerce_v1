import pytest
from django.urls import reverse


# mark.django_db provides this function access to database
@pytest.mark.django_db
def test_root_url(client):
    url = reverse("store:store_index")
    response = client.get(url)
    assert response.status_code == 200
