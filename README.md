# cloud-computing-project-DIT-UTH
ΕΡΓΑΣΙΑ ΣΤΟ ΜΑΘΗΜΑ CLOUD COMPUTING ΠΑΝΕΠΙΣΤΗΜΙΟ ΘΕΣΑΛΛΙΑΣ ΠΛΗΡΟΦΟΡΙΚΗΣ ΚΑΙ ΤΗΛΕΠΙΚΟΙΝΩΝΙΩΝ 2122113 ΜΠΕΛΕΜΕΜΗΣ ΔΗΜΗΤΡΙΟΣ-ΧΡΗΣΤΟΣ
Στο project αυτό γίνεται υλοποίηση και ανάπτυξη μίας cloud-native εφαρμογής χρησιμοποιώντας τεχνολογίες cloud computing. H εφαρμογή παίρνει σαν είσοδο μία εικόνα μέσω HTTP API , γίνεται η επεξεργασία και έπειτα με την χρήση Python βιβλιοθήκες επεξεργασίας εικόνας και επιστρέφςει την τεοποποιημένη εικόνα(grayscale).
Ο βασικός στόχος όμως του project δεν έχει να κάνει με την επεξεργασία της εικόνας , αλλά με το πως μπορούμε να μετατρέψουμε ένα απλό python script σε μία κλιμακώσιμη , distributed και orchestraded cloud-native service.
Στο project υλοποιούνται τα ακόλουθα:
- ανάπτυξη REST API
- containerization με χρήση docker
- cloud deployment principles
- ενορχήστρωση με kubernetes
- δυναμική αυτόματη κλιμάκωση
- αυτοσυντηρούμενη υποδομή
- διαχείριση πόρων
- elastic cloud συμπεριφορά
  
1) Αρχικά η εφαρμοργή υπήρχε σε ένα python script ,όπου παίρνει μία εικόνα και με την χρήση της βιβλιοθήκης OpenCV την μετατρέπει σε grayscale και την αποθηκεύει.
   Παρόλου που το script είναι πολύ απλό και λειτουργικό , υπάρχουν ορισμένοι περιορισμοί (standalone script).
   - μπορούσε να τρέξει μόνο τοπικά
   - δεν υπήρχε web access
   - δεν ήταν δυνατόν να υπάρχει remote επικοινωνία
   - δεν είχε scalability
   - δεν υπήρχε ενορχήτστρωση
   - δεν είχε fault tolerance
   - όχι cloud deployment
   - όχι κατανεμημένη αρχιτεκτονική
     
     Με λίγα λόγια , σε σύγχρονο cloud περιβάλλον αυτή η εφαρμογή δεν θα μπορούσε να σταθεί.
     
2) Έτσι λοιπόν στόχος μας είναι να φτιάξουμε μία cloud native distributed εφαρμογή.
  - Η τελική αρχιτεκτονική έπρεπε:
  - να εκθέτει web API
  - να τρέχει μέσα σε containers
  - να γίνεται deploy σε Kubernetes
  - να κάνει dynamic scaling
  - να υποστηρίζει orchestration
  - να υποστηρίζει self-healing
  - να υποστηρίζει cloud deployment principles

3) Τεχνολογίες που χρησιμοποιήσαμε:
  - Python --> η main γλώσσα προγραμματισμού
  - FastAPI --> REST API framework
  - OpenCV --> για επεξεργασία εικόνας
  - Docker --> για containerization
  - DockerHub --> για image registry
  - Kubernetes --> για container ενορχήστρωση
  - kubectl --> για kubernetes διαχείριση και πλοήγηση
  - HPA -> για αυτόματη κλιμάκωση εφαρμογής
  - github --> version control
4) Χρήση FastAPI:
   Στα cloud-native συστήματα η επικοινωνία γίνεται με APIs.
   Ένα απλό python script δεν έχει την δυνατότητα να επικοινωνήσει με χρήστες,browsers,άλλα services,κατανεμημένα συστήματα,cloud υποδομές.
   Έτσι το script μετατράπηκε σε REST API με FastAPI.
5) Το FastAPI:
   - έχει HHTP endpoints
   - ασύγχρονη επικοινωνία
   - API documentation
   - request validation
   - κλιμάκωση backend αρχιτεκτονικής
   - mircroservice compatibility
   Με αυτόν τον τρόπο μπορούμε να μετατρέψουμε την εφαρμογή μας σε προσβάσιμη web microservice.
6) Αρχιτεκτονική FastAPI:
   Client-->HTTP request-->FastAPI-->επεξεργασία εικόνας-->ανταπόκριση
   (απομακρυσμένη επικοινωνία μέσω HTTp requests)
7)

   
   
   
