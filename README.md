<a name="br1"></a> 

Istraživačka Stanica Petnica

*Ideja za projekat*

Računarstvo

**Cloud**

***Codename: Projekat Mutltivitamin***

Mentor: Nikolina

Polaznici: Andrija Gajić,

Đorđe Radivojević, Sergej Milivojević

Petnica, 2023



<a name="br2"></a> 

Generalna ideja

1\. Internet Protokol Server - Svi

1\.1 U pitanju je socket server koji će morati da čuva podatke, naš izbor je TCP protokol

jer je pouzdaniji i zato što osigurava dostavu podataka. Sa obzirom da nećemo imati

velike zahteve što se tiče efikasnosti i brzine u smilsu velikih prenosa podataka sa puno

korisnika, TCP je bolji izbor.

2\. Rate Limit - Svi

2\.1 Server ima da stalno prima informacije, što znači da je ranjiv na DDoS/DoS napade

sa velikom količinom podataka. Da bi rešili problem DDoS/DoS napada i zapaljivanja

naših servera od preopterećenja rešenje je rate limitovanje bandwith-a po korisniku (Ili

možda sveukupno ako ne radimo sa velikom količinom korisnika). U slučaju da dođe do

napada, serveri imaju više vremena da odreaguju na napad i diskonektuju napadača

zahvaljujući rate limit-u.

3\. CyberSecurity - Svi

3\.1 Svaki server treba da bude u mogćnosti da se zaštiti od napada na njega (DDoS/DoS,

MITM, Brute force, SSH, XSS) jer to može da dovede do onesposobljavanja servera i da

ograniči korisnicima pristup. Rešenje za ovo jeste da se uvede malo Cybersecurity-a i da

npr. Automatski diskonetkuje DoS napadača itd.

4\. Localhost - Sergej

4\.1 Serveri moraju da budu pristupačni za korisnika. Imamo dva načina da hostujemo

server: na lokalnoj mreži i onlajn. Za ovaj sistem plan je da bude lokalan jer onlajn

hostovanje košta novac. Korisnici će moći da pristupe serveru kroz istu Wi-Fi mrežu

preko lokalne IP adrese i porta

5\. GUI - Andrija

5\.1 Za svaku vrstu data servera potrebna je vrsta interfejsa preko koje se pristupa i koristi

sam server. Prosečan korisnik ne bi mogao da koristi terminal a čak i izvrsnom korisniku

je nepraktično. Rešenje je onlajn GUI preko kojeg se pristupa funkcijama sistema i gde se

uploaduju/čitaju fajlovi sa intuitivnim korisničkim interfejsom.



<a name="br3"></a> 

6\. Log-in sistem preko relacione baze podataka - Sergej

6\.1 Moramo na neki način da sprečimo korisnike da interaguju sa fajlovima drugih

korisnika i u isto vreme da verifikujemo njihov identitet radi sigurnosti i verifikacije.

Tehnički pristup ovome je log-in funkcija na GUI koja je povezana na relacionu bazu

podataka u pozadini. Sa radom njih u tandemu osiguravamo bezbednost i verifkaciju

kako korisnika tako i podataka.

7\. Backend - Đjorđe

7\.1 Za korišćene GUI sa samim serverom i povezivanjem svega toga potreban nam je

backend. Moraćemo da povežemo sve to kroz backend (dugmići, fajl submit, log-in

itd…).

8\. Enkripcija (Uz malo soli) - Svi

8\.1 Ne osigurane šifre mogu biti lako pristupljene i maliciozno korišćeni od neovlašćene

strane. Kršenje sistema bi izazvalo katastrofu za privatnost naših korisnika i zaštitu

njihovih podataka. Da bi rešili ovaj problem koristićemo enkripciju preko heš vrednosti

sa soli koja će najverovatnije biti neki podatak od korisnika. Ovo je pouzdana opcija zbog

toga što mala promena u ulaznim podacima pravi veliku promenu u heš vrednosti i

neovlašćene strane neće moći da provale u sistem. I sa tim garantujemo sigurnost naših

korisnika i njihovih podataka.

9\. File system - Sergej

9\.1 Loše organizovan fajl sistem može da dovede do velikih problema kasnije. Ne smemo

da dozvolimo korisnicima da pristupe folderima drugih korisnika i manipulišu njhove

fajlove. Rešenje za ovo je dobro osmišljen fajl sistem sa pametno nameštenim

dozvolama i hierarhijama.

Opciono

1\. Scalability - Andrija

1\.1 Mogućnost proširenja našeg digitalnog oblaka je isto važna stavka ali ne toliko koliko

i kritični sistemi. Bilo bi poželjno da imamo mogućnost da prikačimo druge



<a name="br4"></a> 

mašine/servere da interaguju bez problema sa već postojećom mrežom. Način za ovo

jeste dobro osmišljen kod koji može bez velike muke da se prikači na novu mašinu.

Jednom kad je nakačen na novu mašinu treba da je u mogućnosti da se poveže sa već

postojećom mrežom i bude novi server u našoj mreži. Sve to dok korisniku sa GUI ne

pravi nikakvu razliku.
