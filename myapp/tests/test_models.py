import pytest
from myapp.models import MyModel

@pytest.mark.django_db
def test_my_model():
    obj = MyModel.objects.create(name='Test')
    assert obj.name == 'Test'
