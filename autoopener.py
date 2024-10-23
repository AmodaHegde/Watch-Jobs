import webbrowser
import subprocess

# Set this appropriately depending on your situation
chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
first_url =  "https://web.whatsapp.com/"

# This should open a NEW WINDOW with the URL specified above
command = f"cmd /C \"{chrome_path}\" {first_url} --new-window"

# Alternative way that achieves the same result
# command = f"cmd /C start chrome {first_url} --new-window"

subprocess.Popen(command)

new_tab_urls = [
    "https://mail.google.com/mail/u/0/",   # Gmail
    "https://mail.google.com/mail/u/3/",  # Google Tasks (or any task manager URL)
    "https://calendar.google.com/calendar/u/0/r/tasks",  # Replace with the third website you want to open
    "https://web.telegram.org/k/",
    "https://jobs.sap.com/search/?createNewAlert=false&q=&locationsearch=India&optionsFacetsDD_department=Software-Design+and+Development&optionsFacetsDD_customfield3=Graduate&optionsFacetsDD_country=IN",
    "https://careers.salesforce.com/en/jobs/?search=&country=India&region=Karnataka&team=Software+Engineering&team=Data&team=Enterprise+Technology+%26+Infrastructure&team=Salesforce+Research&pagesize=20#results",
    "https://www.ibm.com/in-en/careers/search?field_keyword_08[0]=Software%20Engineering&field_keyword_08[1]=Infrastructure%20%26%20Technology&field_keyword_08[2]=Data%20%26%20Analytics&field_keyword_08[3]=Cloud&field_keyword_08[4]=Research&field_keyword_18[0]=Entry%20Level&field_keyword_05[0]=India",
    "https://careers.oracle.com/jobs/#en/sites/jobsearch/requisitions?lastSelectedFacet=AttributeChar6&location=India&locationId=300000000106947&selectedCategoriesFacet=300000001917356%3B300000001917338%3B300000001917346&selectedFlexFieldsFacets=%22AttributeChar6%7C0+to+2%2B+years%22&selectedLocationsFacet=300001842985425",
    "https://lseg.wd3.myworkdayjobs.com/en-US/Careers/details/Software-Engineering-QA-Engineer_R0093029?locationCountry=c4f78be1a8f14da0ab49ce1162348a5e&CF_Lookup_Business_Unit_Level_02__Job_Posting_Anchor__Extended=9c1f71183c10016d116d72382401ff75&CF_Lookup_Business_Unit_Level_02__Job_Posting_Anchor__Extended=9c1f71183c100199d5844b382401bf75",
    # Replace with the fourth website you want to open
]

for url in new_tab_urls:
    webbrowser.open_new_tab(url)