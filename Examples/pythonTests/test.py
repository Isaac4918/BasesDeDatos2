from flask import Flask, flash, request, send_file
from werkzeug.utils import secure_filename
import pyodbc
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from ssl import SSLContext, PROTOCOL_TLSv1_2, CERT_NONE
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import io
from flask_cors import CORS
import random
import string

# ===========================================================================
# Cassandra Connection

# Defines the connection string for Cosmos DB and Cassandra
contact_points = ['tfex-cosmos-db-26555.cassandra.cosmos.azure.com']
port = 10350
usernameVar = 'tfex-cosmos-db-26555'
passwordVar = 'wd5uWOiL7UGaYv9W4oyh9VQOEr0FN8JphA71qwM6rnchowByWmv5ldDSfTndVgv9IgsvKEebInagACDbQB5BSw=='
keyspace = 'tfex-cosmos-cassandra-keyspace'

auth_provider = PlainTextAuthProvider(username=usernameVar, password=passwordVar)
ssl_context = SSLContext(PROTOCOL_TLSv1_2)
ssl_context.verify_mode = CERT_NONE

# Creates a Cluster object and a Cassandra session
cluster = Cluster(
    contact_points=contact_points, 
    port=port, 
    auth_provider=auth_provider,
    ssl_context=ssl_context
)
session = cluster.connect(keyspace)

class CassandraConnector():
    def submit(self, user, log):
        session.execute("INSERT INTO userlogs (user_id, logline) VALUES ('"+user+"', '"+log+"')")
        return "Submited"

    def deleteAll(self):
        session.execute("TRUNCATE userlogs")
        return "Deleted all"

    def uploadFile(self, user):
        self.submit(user, "Uploaded File.")

    def downloadFile(self, user):
        self.submit(user, "Downloaded File.")

    def modifyFile(self, user):
        self.submit(user, "Modified File.")

    def deleteFile(self, user):
        self.submit(user, "Deleted File.")

    def userInfoRequested(self, user):
        self.submit(user, "Requested his/her information.")

    def userInfoUpdated(self, user):
        self.submit(user, "Updated his/her information.")

    def userDeleted(self, user):
        self.submit(user, "Deleted his/her account.")

    def signUp(self, user):
        self.submit(user, "Signed up.")

    def userLogin(self, user):
        self.submit(user, "Logged in.")

    def userLogout(self, user):
        self.submit(user, "Logged out.")

    def enrollCourse(self, user):
        self.submit(user, "Enrolled a Course.")

    def unenrollCourse(self, user):
        self.submit(user, "Unenrolled a Course.")

    def availableCourses(self, user):
        self.submit(user, "Viewed available courses.")

    def viewEnrollmentDates(self, user):
        self.submit(user, "Viewed enrollment date.")

    def resetPassword(self, user):
        self.submit(user, "Reset the Password.")

    def viewGradeAverage(self, user):
        self.submit(user, "Viewed grade average.")

    def getEnrollmentReport(self, user):
        self.submit(user, "Viewed enrollment report.")

    def viewEnrolledCourses(self, user):
        self.submit(user, "Viewed enrolled courses.")


logManager = CassandraConnector()

logManager.userLogin("fFri4sRcE0P6oKHtdZ7INR2jwwl2")