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

         - εγκατάσταση missing Linux libraries
         - σωστό configuration dependencies
         - rebuild του Docker image

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

       - centralized image storage
       - deployment source
       - distribution mechanism

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

      Όταν έγινε διαγραφή των pods με :
        kubectl delete pod -l app=image=api
      το kubernetes το δημιούργησε αυτόματα λόγω του desired state του deployment.

  25) Kubernetes networking

      Services:
        Τα pods έχουν όλα προσωρινές IP.Αν τα pods κάνουν επανεκκίνηση οι IP αλλάζουν και έτσι η επικοινωνία σταματά.Έτσι πρέπει να υπάρχει σταθερό networking abstraction.

      Kubernetes Services:

        - σταθερό σημείο πρόσβασης
        - traffic forwarding
        - load balancing
        - service discovery
      το service συνδέει τους χρήστες με τα pods
  26) Nodeport service

      Με το nodeport service η εφαρμογή έγινε exposed μέσω networking port στα cluster nodes.
      Το congifuration περιέχει:

       - external port
       - internal target port
       - pod selectors

  27) Port forwarding

      Το πανεπηστιμιακό kubernetes cluster χρησιμοποιεί restricted networking . Για αυτόν τον λόγο χρησιμοποιήθηκε kubectl port-forward . Με αυτό δημιουργήθηκε ασφαλές local tunnel .
      PC --> KUBERNETES SERVICE --> POD

  28) Πρόσβαση στην εφαρμογή

      Κάναμε port forwarding και έπειτα αποκτήσαμε πρόσβαση στην εφαρμογή μέσω του :
      http://127.0.0.1:8000/docs
      Αφού συνδέθηκε καταλάβαμε ότι το kubernetes networking πέτυχε.

  29) Metrics server

      Για να λειτουργήσει το auto scaling του kubernetes πρέπει νσ έχουμε resource metrics.
      Ένας metrics server δινει πληροφορίες για :

        - cpu metrics
        - memory metrics
        - pod resource usage
      Αποκτήσαμε πρόσβαση σε αυτά μέσω :
        kubectl top pods
      NAME                        CPU   MEMORY
      image-api-584dbcfd8-rhg82   2m    46Mi

        kubectl get pods
      1 Running Pod
      Η CPU βρισκόταν περίπου στο:
              2%
      επομένως δεν υπήρχε λόγος δημιουργίας νέων Pods.
      

  31) Resource requests limits

      Τα requests ορίζουν:

        minimum guaranteed resources
      
      Τα limits ορίζουν:

        maximum allwed resources

      Αυτά είναι αναγκαία για:

        - scheduling
        - κλιμάκωση
        - σταθεροποίηση cluster

  33) CPU requests

      cpu requsts με χρήση millicores
      cpu: "100m"
      δηλαδή 0.1 cpu core
      το kubernetes χρησιμοποιεί αυτές τις τιμές για να υπολογίζει utilization percentages.

  34) Horizontinal Pod Autoscaler (HPA)

      Σε καινούργια cloud συστήματα η προσαρμογή τους πρέπει να γίνεται δυναμικά.
      χωρις αυτόματη κλιμάκωση :

        - σπατάλη πόρων
        - η απόδοση πέφτει σε traffic spikes
        - το infrastructure γίνεται inefficient
      Το HPA έβλεπε το cpu utilization και προσάρμοζε ανάλογα δυναμικά.
      1. συλλογή metrics
      2. υπολογισμός μέσου φορτίου
      3. σύγκριση με threshold
      4. απόφαση κλιμάκωσης
      5. δημιουργία ή διαγραφή pods

      Δημιουργήθηκε το αρχείο hpa.yaml . Το HPA συνδέθηκε με το deployment της εφαρμογής.
      minReplicas: 1 ( η εφαρμογή θα έχει πάντα τουλάχιστον ένα pod)
      maxReplicas: 5 ( η εφαρμογή μπορεί να έχει μέχρι max 5 pod )
      averageUtilization: 50 ( όταν η μέση χρήση της cpu ξεπεράσει το 50% τότε γίνεται scale up)

      Στόχος του πειράματος ήταν να δούμε ότι το HPA παρακολουθεί την χρήση της cpu , το kubernetes δημιουργεί καινούργια pods , η εφαρμογή κλιμακώνεται αυτόματα.

      Για να παρακολουθούμε το HPA :
      kubectl get hpa -w ( -w συνεχής παρακολούθηση αλλαγών )
      επίσης σε άλλο terminal :
      kubectl get pods -w  , ώστε να παρακολουθείται η δημιουργία νέων Pods σε πραγματικό χρόνο.

      Για να αυξηθεί η χρήση CPU χρησιμοποιήθηκε εργαλείο load testing.
      Η διαδικασία δημιούργησε μεγάλο αριθμό ταυτόχρονων αιτήσεων προς την εφαρμογή.
      Το φορτίο αυτό προσομοίωνε πολλούς ταυτόχρονους χρήστες.

      Κατά τη διάρκεια του πειράματος παρατηρήθηκαν τιμές:

        cpu: 2%
        cpu: 3%
        cpu: 124%
        cpu: 428%

      Οι τιμές αυτές ξεπέρασαν σημαντικά το threshold του 50%.
      Όταν η χρήση CPU ξεπέρασε το όριο:

        50%

      το HPA αποφάσισε να αυξήσει τον αριθμό των replicas.

      Παρατηρήθηκε:

        Replicas: 1
        Replicas: 4
        Replicas: 5

      Δημιουργία Νέων Pods

          Το Kubernetes δημιούργησε δυναμικά νέα Pods.
          Παρατηρήθηκαν καταστάσεις:
              Pending  ,  Το Pod έχει προγραμματιστεί αλλά δεν έχει ξεκινήσει , Το Scheduler αναζητά διαθέσιμους πόρους .
          στη συνέχεια:
              ContainerCreating , το node κατεβάζει image , δημιουργεί container , ξεκινά την εφαρμογή .
          και τελικά:
              Running , Η εφαρμογή είναι πλήρως λειτουργική και έτοιμη να δεχτεί αιτήματα.
      
          Η εφαρμογή μετατράπηκε από:
              1 Pod
          σε:
              5 Pods
          χωρίς καμία χειροκίνητη παρέμβαση.Αυτό αποτελεί άμεση απόδειξη επιτυχημένου auto scaling.

      Load Balancing

        Μετά τη δημιουργία νέων Pods, το Kubernetes Service συνέχισε να δέχεται τα αιτήματα των χρηστών , το Service διένειμε τα αιτήματα αυτόματα στα διαθέσιμα Pods.
        
        Έτσι επιτεύχθηκε:
         - καλύτερη απόδοση
         - καλύτερη αξιοποίηση πόρων
         - υψηλότερη διαθεσιμότητα

      SELF HEALING

        Πραγματοποιήθηκε δοκιμή διαγράφοντας χειροκίνητα τα Pods:
          kubectl delete pod -l app=image-api
      
        Παρότι τα Pods διαγράφηκαν, το Deployment παρέμεινε ενεργό , το Kubernetes εντόπισε ότι ο πραγματικός αριθμός Pods ήταν μικρότερος από τον επιθυμητό.
        Το Kubernetes δημιούργησε νέα Pods αυτόματα , η εφαρμογή επανήλθε σε πλήρη λειτουργία χωρίς καμία ανθρώπινη παρέμβαση.

        Το self-healing αποτελεί βασικό χαρακτηριστικό των cloud-native εφαρμογών.

          Παρέχει:
           - υψηλή διαθεσιμότητα
           - ανοχή σε σφάλματα
           - αυτόματη αποκατάσταση βλαβών
      

        ΣΥΜΠΕΡΑΣΜΑΤΑ

              Το αρχικό standalone Python script μετατράπηκε επιτυχώς σε cloud-native εφαρμογή.
              Η τελική λύση υποστηρίζει:

                 - REST API
                 - Containerization
                 - Kubernetes orchestration
                 - Dynamic scaling
                 - Service discovery
                 - Self-healing
                 - Load balancing

            Κατά την ανάπτυξη του project εφαρμόστηκαν στην πράξη:

             - Cloud-Native Architecture
             - Microservices
             - Containerization
             - Container Orchestration
             - Scalability
             - Elasticity
             - Self-Healing Systems
             - Distributed Computing
             - Resource Optimization
             - Infrastructure Automation

          Το project απέδειξε ότι ακόμη και μια απλή εφαρμογή επεξεργασίας εικόνας μπορεί να μετατραπεί σε μια πλήρως cloud-native υπηρεσία χρησιμοποιώντας σύγχρονες τεχνολογίες                 containerization και orchestration.

          Η χρήση Docker και Kubernetes επέτρεψε:

           - αυτοματοποίηση ανάπτυξης
           - δυναμική κλιμάκωση
           - αυτόματη ανάκτηση από σφάλματα
           - αποδοτική χρήση πόρων

          αποδεικνύοντας στην πράξη τις βασικές αρχές του Cloud Computing.
          





   
   
   
