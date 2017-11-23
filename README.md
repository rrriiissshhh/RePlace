# RePlace
Placement Portal IITB
### How to run?
Run the following commands in the same directory as the fetched repo.
```
source env/bin/activate
pip3 install -r requirements.txt
python src/manage.py runserver
```

Update database before trying to run the server
```
./updatedb
```

push database updates to repository
```
./dumpdb
git add datadump
git commit -m "message"
git push origin master
```

Open [127.0.0.1:8000](http://127.0.0.1:8000/) to get to the home page of **RePlace**.

 
### Status 
- Login pages for company, student and coordinator combined
- Logout created
- All static files in one place
- Show basic jaf information 
- Parallax in home page
- Home page scroll animation
- Error display mechanism on login pages
- Models created

- Parallax improving LATER

#### Company
- Company registration form created 
- Jaf creation form almost complete
- Post company jaf form (partial)

#### IC
- Make resume upload, view
- IC tabs for resume selection status (posting the form remaining) SOURABH, backend DEPAL
- Update​ database​ regarding​ ​test​​ location,​​ timing​ ​and​​ other​ updates (date parsing error) DEPAL

#### Student
- Student Home page done
- Filters for students done
- Provide​ ​reviews​ ​for​ completed​ internships
- Signing/Unsigning JAF
- View Past JAF Data
- Make sign jaf view

### Plans 
- Login​ ​ and​ ​ Logout​ ​ for​ ​ all​ ​ users (DONE)

#### Admin
- Initially​ ​ populate​ ​ the​ ​ database (DONE)
- Update​ ​ database​ ​ at​ ​ end​ ​ of​ ​ the​ ​ semester/year​ ​ regarding​ ​ new​ ​ admissions,​ ​ CPI change​ ​ etc,.​ ​ (if​ ​ time​ ​ permits) (CANCEL)
- This​ ​ part​ ​ represents​ ​ the​ ​ connections​ ​ of​ ​ our​ ​ project​ ​ with​ ​ rest​ ​ of​ ​ database​ ​ tables​ ​ in the​ ​ university (CANCEL)

#### Student
- Provide​ ​ reviews​ ​ for​ ​ completed​ ​ internships (DONE)
- View​ ​ and​ ​ Sign​/Unsign​ eligible​ ​ JAFs (DONE)
- Search​ ​ current​ ​ JAFs​ ​ according​ ​ to​ ​ various​ ​ filters (DONE)
- View​ ​ all​ ​ data​ ​ regarding​ ​ past​ ​ interns​ ​ including​ ​ reviews,​ ​ selections​ ​ and​ ​ procedures (DONE) RISH
- Upload​ ​ resume​ ​ and​ ​ see​ ​ status​ ​ of​ ​ verification​ (if​ ​ time​ ​ permits) (PARTIAL) SOURABH
- Confirm​ ​ final​ ​ selection​ ​ for​ ​ students​ ​ finally​ ​ shortlisted​ ​ by​ ​ companies (CANCEL) 
- View training blog (PARTIAL) RISH

#### IC
- Verify​ ​ resumes (PARTIAL) SOURABH 
- Update​ database​ ​ regarding​ ​ test​ ​ location,​ ​ timing​ ​ and​ ​ other​ ​ updates (PARTIAL) MEET

#### Company
- Create​ ​ JAFs​ ​ and​ ​ see​ ​ specific​ ​ resume​ ​ number​ ​ of​ ​ applicants (PARTIAL) DEPAL, RISH
- Set​ ​ eligibility​ ​ conditions (DONE) 
- Shortlist​ ​ based​ ​ on​ ​ the​ ​ resumes​ ​ of​ ​ applicants (PARTIAL) SOURABH
- See​ ​ progress​ ​ level​ ​ of​ ​ shortlisted​ ​ students​ ​ according​ ​ to​ ​ various​ ​ sequential​ ​ tests​ ( ​if time​ ​ permits) (NOPE) SOURABH
- Give​ ​ final​ ​ selections​ ​ and​ ​ see​ ​ the​ ​ confirmation​ ​ status​ ​ by​ ​ selected​ ​ students. (PARTIAL) SOURABH


### Filers 
- Company category
- Signed, Unsigned
- CPI (later) (range)
- Stipend (range)
- Can sign
- Job Profile
- Pre deadline
