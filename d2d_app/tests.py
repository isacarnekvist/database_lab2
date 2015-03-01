from django.test import TestCase
from d2d_app.models import *
from django.contrib.auth.models import User

class TestCorrectness(TestCase):
    """ Tests inserting new data with relationships and check that they are as expected """
    def setUp(self):
        u1 = User.objects.create_user(username='test1@kth.se', password='password')
        u2 = User.objects.create_user(username='test2@kth.se', password='password')
        cu1 = Customer.objects.create(user=u1, bankAccountNo=1234567890)
        cu2 = Customer.objects.create(user=u2)
        p1 = Package.objects.create(description='En liten grej',
                                         height=200,
                                          width=100,
                                         length=300,
                                          price=1000,
                                         weight=500)
        p2= Package.objects.create(description='En annan grej',
                                         height=200,
                                          width=100,
                                         length=300,
                                          price=1000,
                                         weight=500)
        cnt1 = Contract.objects.create(seller=cu1, buyer=cu2, package=p1)
        cnt2 = Contract.objects.create(seller=cu2, buyer=cu1, package=p2)

    def test_details(self):
        pass
        
    def test_relations(self):
        pass
