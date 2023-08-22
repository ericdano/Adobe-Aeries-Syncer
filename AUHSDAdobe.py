import io, ftplib, ssl, sys, os, datetime, json, smtplib, logging
from pathlib import Path
from umapi_client import Connection, OAuthS2S, UserQuery, GroupsQuery, UserAction
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from logging.handlers import SysLogHandler

class RemoveUser(UserEmail):

class AddUser(UserEmail):

class RemoveUserFromAll(UserEmail):
    user = UserAction(UserEmail)
    user.remove_from_groups(all_groups=True)
    conn.execute_single(user,immesiate=True)
    

if __name__ == '__main__':
    confighome = Path.home() / ".Acalanes" / "Acalanes.json"
    with open(confighome) as f:
        configs = json.load(f)
    thelogger = logging.getLogger('MyLogger')
    thelogger.setLevel(logging.DEBUG)
    handler = logging.handlers.SysLogHandler(address = (configs['logserveraddress'],514))
    thelogger.addHandler(handler)
    #prep status (msg) email
    msg = EmailMessage()
    msg['From'] = configs['SMTPAddressFrom']
    msg['To'] = "serveradmins@auhsdschools.org"
    msgbody = ''
    WasThereAnError = False
    oauth = OAuthS2S(
    client_id=configs['AdobeClientID'],
    client_secret=configs['AdobeClientSecret'])

    conn = Connection(org_id=configs['AdobeOrgID'], auth=oauth)
    print(conn.status())
    user = UserQuery(conn, "edannewitz@auhsdschools.org").result()
    if user is not None:
        print(user)
    groups = GroupsQuery(conn)
    for group in groups:
        print(group)

