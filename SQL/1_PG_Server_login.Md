# PostgreSQL এ Login করার নিয়ম

## Windows / Mac / Linux সব জায়গায় সাধারণ কমান্ড:
```bash
psql -U <username> -d <database_name>
```

## 📌 যদি database_name না দাও, তাহলে user name-এই database খুলবে:
```bash
psql -U <username>
```
🔐 Password চাইলে Enter করতে হবে।


## যদি সার্ভার অন্য কোনো মেশিনে থাকে, তাহলে হোস্ট অ্যাড্রেস উল্লেখ করতে হবে:
```bash
psql -h <host_address> -U <username> -d <database_name>
```

#### NOTE:- Environment Variables path add করে দিলে প্রতিবার username host_address দিতে হবে না।
```bash
C:\Program Files\PostgreSQL\17\bin
```

### 🟦 Example
```bash
C:\Users\Rakib>psql -U postgres
Password for user postgres:

psql (17.2)
WARNING: Console code page (437) differs from Windows code page (1252)
         8-bit characters might not work correctly. See psql reference
         page "Notes for Windows users" for details.
Type "help" for help.

postgres=#
```