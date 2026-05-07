#include<iostream>
#include<fstream>
#include<string>
using namespace std;

class user {
    string username, email, password;
    fstream file;

public:
    void login();
    void signup();
    void forget();
} obj;

int main() {
    char choice;
    while (true) { // Added a loop so the program doesn't close after one action
        cout << "\n1- Login";
        cout << "\n2- Sign-Up";
        cout << "\n3- Forget Password!";
        cout << "\n4- Exit";
        cout << "\nEnter Your Choice :: ";
        cin >> choice;
        cin.ignore(); // Clears the newline character from the buffer

        switch (choice) {
            case '1':
                obj.login();
                break;
            case '2':
                obj.signup();
                break;
            case '3':
                obj.forget();
                break;
            case '4':
                return 0;
            default:
                cout << "Invalid Selection...!";
        }
    }
}

void user::signup() {
    cout << "\nEnter your username here :: ";
    getline(cin, username);

    cout << "Enter your email address :: ";
    getline(cin, email);

    cout << "Enter your password :: ";
    getline(cin, password);

    // Using one consistent filename: "loginData.txt"
    file.open("loginData.txt", ios::out | ios::app);
    file << username << "*" << email << "*" << password << endl;
    file.close();
    cout << "Signup Successful!\n";
}

void user::login() {
    string searchName, searchPass;
    bool found = false;
    
    cout << "-----------LOGIN------------" << endl;
    cout << "Enter your username :: ";
    getline(cin, searchName);
    cout << "Enter your password :: ";
    getline(cin, searchPass);

    file.open("loginData.txt", ios::in);
    // Read formatted data: stop at * for name/email, and \n for password
    while (getline(file, username, '*') && 
           getline(file, email, '*') && 
           getline(file, password, '\n')) {
        
        if (username == searchName && password == searchPass) {
            cout << "\nAccount Login Successful...!";
            cout << "\nUsername :: " << username << endl;
            cout << "Email    :: " << email << endl;
            found = true;
            break;
        }
    }
    if (!found) {
        cout << "\nInvalid username or password!";
    }
    file.close();
}

void user::forget() {
    string searchName, searchEmail;
    bool found = false;
    
    cout << "\nEnter Your Username :: ";
    getline(cin, searchName);
    cout << "Enter Your Email Address :: ";
    getline(cin, searchEmail);

    file.open("loginData.txt", ios::in);
    while (getline(file, username, '*') && 
           getline(file, email, '*') && 
           getline(file, password, '\n')) {
        
        if (username == searchName && email == searchEmail) {
            cout << "\nAccount Found...!" << endl;
            cout << "Your Password :: " << password << endl;
            found = true;
            break;
        }
    }
    if (!found) {
        cout << "\nAccount not found or details incorrect!";
    }
    file.close();
}