# Socket Programming – Programming Assignment 1

## Author

Aa’dil Khamis Ngangila

---

## Project Overview

This project implements a **TCP client-server application** using Python sockets.

The system consists of:

* A **Server program**
* A **Client program**

The client sends:

* Its name
* An integer between 1 and 100

The server:

* Displays both names
* Chooses its own integer
* Computes and displays the sum
* Sends its name and integer back to the client

The client then:

* Displays both values
* Computes and verifies the sum
* Terminates properly

This implementation follows the assignment specification exactly.

---

## Network Configuration

* **Protocol:** TCP
* **Port Number:** 6000 (greater than 5000 as required)
* **Message Format:**

```
Name|Integer
```

Example:

```
Client of Aa’dil Khamis Ngangila|25
```

The delimiter `|` is used for parsing.

---

## Files Included

```
server.py     → TCP server implementation
client.py     → TCP client implementation
README.md     → Project documentation
```

---

## How the Program Works

### Server

1. Creates a TCP socket
2. Binds to port 6000
3. Listens for incoming client connections
4. Accepts connection
5. Receives client message
6. Extracts client name and number
7. Validates integer range (1–100)
8. Chooses its own integer (50)
9. Computes sum
10. Sends response back to client
11. Closes connection

If the server receives a number outside the valid range, it:

* Prints error message
* Closes sockets
* Terminates

---

### Client

1. Prompts user for integer (1–100)
2. Connects to server
3. Sends name and integer
4. Receives server response
5. Displays both names and numbers
6. Computes sum locally
7. Closes socket
8. Terminates

---

## Running Instructions

### Requirements

* Python 3.x
* No external libraries required

---

### Step 1: Start the Server

Open a terminal and run:

```
python server.py
```

You should see:

```
[SERVER] Server of Aa’dil Khamis Ngangila is running on port 6000...
```

---

### Step 2: Run the Client

Open a second terminal and run:

```
python client.py
```

Enter an integer between 1 and 100 when prompted.

---

## Example Execution

### Client Input

```
Enter an integer between 1 and 100: 25
```

### Server Output

```
Client Name: Client of Aa’dil Khamis Ngangila
Server Name: Server of Aa’dil Khamis Ngangila
Client Number: 25
Server Number: 50
Sum: 75
```

### Client Output

```
Server Name: Server of Aa’dil Khamis Ngangila
Client Number: 25
Server Number: 50
Sum: 75
```

---

## Testing Performed

The following test cases were executed:

* Normal case (e.g., 25)
* Lower boundary (1)
* Upper boundary (100)
* Invalid input (e.g., 150 → server shutdown)
* Multiple sequential client connections

All valid cases produced correct sums.

---

## Design Decisions

* TCP chosen for reliable communication
* Fixed server integer (50) for deterministic testing
* Simple string protocol using delimiter
* Sequential (non-concurrent) server for simplicity

---

## Limitations

* Server handles one client at a time
* No encryption
* No GUI
* No persistent logging

---

## Possible Improvements

* Implement multi-threaded server
* Use JSON message format
* Add logging system
* Add input validation on client side
* Implement random server integer
* Add GUI interface

---

## Academic Integrity

This project was developed independently in accordance with the course requirements.

---

If you'd like, I can now create:

* A more advanced README (professional GitHub style with badges)
* A concurrent (threaded) server version
* A polished design document ready for PDF submission
* Or help you prepare the extra credit version
Below is a **clean, submission-ready `README.md`** for your GitHub repository.
It is written in professional technical style suitable for grading.

You can copy this directly into your `README.md` file.

---

# Socket Programming – Programming Assignment 1

## Author

Aa’dil Khamis Ngangila

---

## Project Overview

This project implements a **TCP client-server application** using Python sockets.

The system consists of:

* A **Server program**
* A **Client program**

The client sends:

* Its name
* An integer between 1 and 100

The server:

* Displays both names
* Chooses its own integer
* Computes and displays the sum
* Sends its name and integer back to the client

The client then:

* Displays both values
* Computes and verifies the sum
* Terminates properly

This implementation follows the assignment specification exactly.

---

## Network Configuration

* **Protocol:** TCP
* **Port Number:** 6000 (greater than 5000 as required)
* **Message Format:**

```
Name|Integer
```

Example:

```
Client of Aa’dil Khamis Ngangila|25
```

The delimiter `|` is used for parsing.

---

## Files Included

```
server.py     → TCP server implementation
client.py     → TCP client implementation
README.md     → Project documentation
```

---

## How the Program Works

### Server

1. Creates a TCP socket
2. Binds to port 6000
3. Listens for incoming client connections
4. Accepts connection
5. Receives client message
6. Extracts client name and number
7. Validates integer range (1–100)
8. Chooses its own integer (50)
9. Computes sum
10. Sends response back to client
11. Closes connection

If the server receives a number outside the valid range, it:

* Prints error message
* Closes sockets
* Terminates

---

### Client

1. Prompts user for integer (1–100)
2. Connects to server
3. Sends name and integer
4. Receives server response
5. Displays both names and numbers
6. Computes sum locally
7. Closes socket
8. Terminates

---

## Running Instructions

### Requirements

* Python 3.x
* No external libraries required

---

### Step 1: Start the Server

Open a terminal and run:

```
python server.py
```

You should see:

```
[SERVER] Server of Aa’dil Khamis Ngangila is running on port 6000...
```

---

### Step 2: Run the Client

Open a second terminal and run:

```
python client.py
```

Enter an integer between 1 and 100 when prompted.

---

## Example Execution

### Client Input

```
Enter an integer between 1 and 100: 25
```

### Server Output

```
Client Name: Client of Aa’dil Khamis Ngangila
Server Name: Server of Aa’dil Khamis Ngangila
Client Number: 25
Server Number: 50
Sum: 75
```

### Client Output

```
Server Name: Server of Aa’dil Khamis Ngangila
Client Number: 25
Server Number: 50
Sum: 75
```

---

## Testing Performed

The following test cases were executed:

* Normal case (e.g., 25)
* Lower boundary (1)
* Upper boundary (100)
* Invalid input (e.g., 150 → server shutdown)
* Multiple sequential client connections

All valid cases produced correct sums.

---

## Design Decisions

* TCP chosen for reliable communication
* Fixed server integer (50) for deterministic testing
* Simple string protocol using delimiter
* Sequential (non-concurrent) server for simplicity

---

## Limitations

* Server handles one client at a time
* No encryption
* No GUI
* No persistent logging

---

## Academic Integrity

This project was developed independently in accordance with the course requirements.

---


