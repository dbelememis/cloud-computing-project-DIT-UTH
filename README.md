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
  - 
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
   
7) API endpoint:

  POST/grayscale
  Παίρνει μία uploaded εικόνα , γίνεται επεξεργασία με OpenCV , γίνεται μετατροπή σε grayscale , επιστροφή της επεξεργασμένης εικόνας.
  
8) Swagger:
   
  Το FastAPI διαθέτει αυτόματο API documentation. Έτσι το FastAPI δημιουργεί αυτόματα Swagger UI και OpenAPI schema.Έπειτα το documentation γίνεται διαθέσιμο μέσω http://127.0.0.1:8000/docs . Με αυτόν τον τρόπο το testing και το development έγιναν πολύ πιο απλά.

9) Docker και Containerization:
    
    Το kubernetes δεν μπορεί να κάνει deploy raw python scriptakia , έτσι το kubernetes κάνει deploy containers. Για αυτόν τον λόγο το application πρέπει να γίνει containerized.
    Αυτό θα γίνει με την χρήση docker. To πακετάρισμα περιέχει python runtime , dependencies , FastAPI application , OpenCV βιβλιοθήκες , source code. ( αυτό γίνεται σε ένα απομωνομένο περιβάλλον εκτέλεσης.
10) Containers:

    Ένα container είναι ένα isolated execution environment το οποίο περιέχει:
    
    - components λειτουργικού συστήματος
    - runtime environment
    - libraries
    - app code

    Τα container μπορούν να εγγυηθούν consistency μεταξύ environments . Έτσι , μία εφαρμογή θα έχει την ίδια συμπεριφορά σε τοπικά μηχανήματα , σε servers , σε kubernetes clusters.
    
12) Dockerfiles:

    Το dockerfile δημιουργήθηκε έτσι ώστε να περιγράψει πως θα χτιστεί η εικόνα της εφαρμογής.
    Το dockerfile περιέχει:
    
    - python base image
    - application files
    - dependency installation
    - FastAPI startup command
      
  13) Docker build διαδικασία:

      Χτίσαμε το image με την εντολή:
      docker  build -t image-api .
      Με αυτήν την εντολή δημιουργήσαμε ένα επαναχρησιμοποιούμενο image που περιέχει ολοκλήρη την εφαρμογή.

  14) Εκτέλεση container :

      Το container εκτελέστηκε τοπικά με την :
      docker run -p 8000:8000 image-api
      Εδώ το API έγινε προσβάσιμο τοπικά , το FastAPI τρέχει μέσα σε container , η εφαρμογή έγινε cloud-ready.

  15) Πρόβλημα με OpenCV dependency issues :

      Κατά την εκτέλεση του container εμφανίστηκαν dependency issues με το OpenCV.
      error: libGL.so.1 missing
      εμφανίστηκε επειδή κάποιες system libraries που απαιτούνται από το OpenCV δεν υπήρχαν μέσα στο container.
      
  16) Λύση των issues :

      Το πρόβλημα λύθηκε με:

          εγκατάσταση missing Linux libraries

          σωστό configuration dependencies

          rebuild του Docker image

      Αυτό ανέδειξε ένα σημαντικό cloud concept:

      Dependency management μέσα στα containers.

  17) Docker Hub registry :

      Το kubernetes cluster δεν μπορούσε να προσπελάσει local docker images . Έτσι , έπρεπε να γίνει remote image registry και για αυτό χρησιμοποιήθηκε το docker hub ως image registry.

  18) Image push :

      το image έγινε tag και upload με :
      
      docker tag image-api dbelememis/image-api:v1
      docker push dbelememis/image-api:v1

      έτσι το kubernetes cluster απέκτησε πρόσβαση και μπορούσε να κατβάσει την εικόνα remotely.

  19) Cloud registry concept :

      Ένα container registry λειτοργεί ως :

        centralized image storage

        deployment source

        distribution mechanism

      αυτή είναι η βασική έννοια των cloud-native deployment αρχιτεκτωνικών.

  20) Kubernetes :

      Το docker απλώς τρέχει containers. Το kubernetes προσφέρει :
        - ενορχήστρωση
        - scheduling
        - δικτύωση
        - κλιμάκωση
        - self healing
        - lifecycle διαχείρηση
      Το kubernetes έχει την δυνατότητα να παίρνει τα απομωνομένα containers και να τα μετατρέπει σε κατανεμημένα cloud applications.

  21) deployment yaml

      Φτιάξαμε ένα deploymen.yaml . Το deployment περιγράφει:

        - τον επιθυμητό αριθμό replicas
        - το container image
        - ports
        - resource configuration

      Το kubernetes προσπαθεί συνέχεια να κρατήσει αυτό το επιθυμητό state.

  22) Kubernetes pods

      Το kubernetes τρέχει τις εφαρμογές μέσα σε pods. Ένα pod :
      
        - αντιπροσωπευεί ένα ή περισσότερα containers
        - αντιπροσωπευεί network identity
        - execution unit μέσα σε kubernetes

      Η εφαρμορή έγινε deploy ωε kubernetes pods .

  23) Deployment διαδικασία

      Το deployment έγινε με την ακόλουθη εντολή:
      
      kubectl apply -f deployment.yaml
      
      Τώρα το kubernetes :
      - έφτιαξε pods
      - έκανε pull τα docker images
      - έγινε εκκίνηση των containers
      - έκανε αυτόματη διαχείρηση της εκτέλεσης

  24) Kubernetes self-healing

      








   
   
   
