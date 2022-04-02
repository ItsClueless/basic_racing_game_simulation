/* graphics.cpp will be responsible for running the program and starting the file execution
 * Start by getting user username and password, pass to a file
 * Try finding username/password. If not it'll say wrong name/password, Try again or start a new user
 * and get password and start coins at 0
 * Then it'll start the python execution, passing in the username and coins.
 * Then it'll run the game, and then start the graphics after a certain point is reached
 */
#include "graphics.h"
#include "circle.h"
#include "rect.h"
#include <iostream>
#include <memory>
#include <vector>
#include <ctime>
#include <fstream>
using namespace std;
#ifdef _WIN32
const string python = "py";
#else
const string python = "python3";
#endif


GLdouble width, height;
int wd;

const color white(1, 1, 1);
const color red(1,0,0);
const color blue(0,0,1);
const color black(0, 0, 0);
const color grey(.7, .7, .7);
const color yellow(1,1,0);
const color skyBlue(1/255.0, 110/255.0, 214/255.0);

Rect road;
vector<unique_ptr<Shape>> user;
vector<unique_ptr<Shape>> opponent;
vector<Rect> yellowLine;
vector<unique_ptr<Shape>> clouds;

bool havePlayed() {
    string input;
    cout << "Have you played before(y/n): " << endl;
    getline(cin, input);


    while (input.size() != 1 || tolower(input[0]) != 'y' && tolower(input[0]) != 'n') {
        cout << "INVALID INPUT" << endl;
        cout << "Enter either (y) for yes, (n) for no: " << endl;
        getline(cin, input);
    }
    if (tolower(input[0]) == 'y') {
        return true;
    }
    return false;
}


string getUserName(){
    string input;
    cout << "Enter your username: " << endl;
    getline(cin,input);

    while (input == "") {
        if (cin) {
            cin >> input;
        }
        else{
            cout << "Enter again: " << endl;
            cin.clear();
            getline(cin,input);
        }
    }
    return input;
}

string getUserPassword(){
    string input;
    string junk;
    cout << "Enter your password: " << endl;
    getline(cin,input);

    while (input == "") {
        if (cin) {
            cin >> input;
        }
        else{
            cout << "Enter again: " << endl;
            cin.clear();
            getline(cin,input);
        }
    }
    return input;
}

string getUserCoins(string name, string password){
    // Open the file
    ifstream inFile("../racing_game_users.txt");
    string coins = "";
    string junk;
    string userName;
    string userPass;
    string newline;
    getline(inFile, userName);
    while (inFile && coins == "") {
        if (userName == name) {
            getline(inFile, userPass);
            while (userPass != password) {
                cout << "Incorrect password. Please try again" << endl;
                password = getUserPassword();
            }
            if (userPass == password) {
                getline(inFile, coins);

                inFile.close();
                return coins;
            }
        }
        getline(inFile, userName);
    }
    cout << "Username not found." << endl;
    inFile.close();
    return "500";
}

void createUser(string name, string pass, string coins){
    // Create and open files to write the reads
    // Named accordingly the different hash tables
    ofstream userRecords;
    userRecords.open("../racing_game_users.txt", ios_base::app);
    userRecords << '\n' + name << endl;
    userRecords << pass << endl;
    userRecords << coins;
    userRecords.close();
}

bool starter(){
    string command;
    string coins = "500";
    bool playedBefore = havePlayed();
    if (!playedBefore){
        cout << "Please create a new user to save your progress" << endl;
    }
    string userName = getUserName();
    string userPassword = getUserPassword();
    if (playedBefore){
        coins = getUserCoins(userName, userPassword);
    }
    else{
        createUser(userName,userPassword, coins);
    }

    cout << "coins total " << coins << endl;
    string play = "yes";

    //Use command-line arguments to pass the filenames to the Python file
    command =  python + " ../racing_game_simulation.py " +  userName + " " + play + " " + coins;
    system(command.c_str());
    return true;
}

void initUser() {
    user.clear();
    dimensions userBody(40,10);
    dimensions userUpperBody(20,10);

    user.push_back(make_unique<Circle>(white,20,255,5)); //color,x,y,r
    user.push_back(make_unique<Circle>(white,40,255,5));
    user.push_back(make_unique<Rect>(red,30,250,userBody));
    user.push_back(make_unique<Rect>(red,30,245,userUpperBody));
}

void initOpponent() {
    opponent.clear();
    dimensions opponentBody(40,10);
    dimensions opponentUpperBody(20,10);

    opponent.push_back(make_unique<Circle>(white,20,355,5)); //color,x,y,r
    opponent.push_back(make_unique<Circle>(white,40,355,5));
    opponent.push_back(make_unique<Rect>(blue,30,350,opponentBody));
    opponent.push_back(make_unique<Rect>(blue,30,345,opponentUpperBody));
}

void initRoad() {
    road.setCenter(width/2, 300);
    road.setSize(width, 150);
    road.setColor(black);
}

void initYellowLine(){
    dimensions yellowLineDim (20,5);
    for (int i = 0; i < width; i += 30) {
        yellowLine.push_back(Rect(yellow, i, 300, yellowLineDim));
    }
}

void initClouds() {
    clouds.clear();

    clouds.push_back(make_unique<Circle>(white, 300, 100, 20));
    clouds.push_back(make_unique<Circle>(white, 330, 100, 20));
    clouds.push_back(make_unique<Circle>(white, 320, 90, 20));

    clouds.push_back(make_unique<Circle>(white, 20, 90, 30));
    clouds.push_back(make_unique<Circle>(white, 50, 90, 30));
    clouds.push_back(make_unique<Circle>(white, 40, 60, 30));

    clouds.push_back(make_unique<Circle>(white, 450, 60, 30));
    clouds.push_back(make_unique<Circle>(white, 480, 60, 30));
    clouds.push_back(make_unique<Circle>(white, 470, 30, 25));

    clouds.push_back(make_unique<Circle>(white, 955, 40, 20));
    clouds.push_back(make_unique<Circle>(white, 980, 40, 20));
    clouds.push_back(make_unique<Circle>(white, 970, 35, 20));

    clouds.push_back(make_unique<Circle>(white, 800, 60, 20));
    clouds.push_back(make_unique<Circle>(white, 830, 60, 20));
    clouds.push_back(make_unique<Circle>(white, 820, 70, 20));

    clouds.push_back(make_unique<Circle>(white, 1075, 45, 20));
    clouds.push_back(make_unique<Circle>(white, 1090, 50, 20));
    clouds.push_back(make_unique<Circle>(white, 1070, 50, 20));

}

void init() {
    width = 1000;
    height = 400;
    srand(time(0));
    initRoad();
    initYellowLine();
    initUser();
    initOpponent();
    initClouds();
}

/* Initialize OpenGL Graphics */
void initGL() {
    // Set "clearing" or background color
    glClearColor(skyBlue.red, skyBlue.green, skyBlue.blue, 1.0f);
}

/* Handler for window-repaint event. Call back when the window first appears and
 whenever the window needs to be re-painted. */
void display() {
    // Tell OpenGL to use the whole window for drawing
    glViewport(0, 0, width, height); // DO NOT CHANGE THIS LINE (unless you are running Catalina on Mac)

    // Do an orthographic parallel projection with the coordinate
    // system set to first quadrant, limited by screen/window size
    glMatrixMode(GL_PROJECTION); // DO NOT CHANGE THIS LINE
    glLoadIdentity(); // DO NOT CHANGE THIS LINE
    glOrtho(0.0, width, height, 0.0, -1.f, 1.f); // DO NOT CHANGE THIS LINE

    // Clear the color buffer with current clearing color
    glClear(GL_COLOR_BUFFER_BIT); // DO NOT CHANGE THIS LINE

    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL); // DO NOT CHANGE THIS LINE

    /*
     * Draw here
     */
    road.draw();

    for (Rect &y : yellowLine) {
        y.draw();
    }

    //Draw user
    for (unique_ptr<Shape> &u : user) {
        u->draw();
    }

    for (unique_ptr<Shape> &o : opponent) {
        o->draw();
    }

    for (unique_ptr<Shape> &s : clouds) {
        s->draw();
    }

    if (user[2]->getRightX() >= width){
        glutDestroyWindow(wd);
        cout << "\nEnding Simulation" << endl;
        string command;
        command =  python + " ../game_ending.py ";
        system(command.c_str());
        remove("../game_file.txt.");
        exit(0);
    }

    if (opponent[2]->getRightX() >= width){
        glutDestroyWindow(wd);
        cout << "\nEnding Simulation" << endl;
        string command;
        command =  python + " ../game_ending.py ";
        system(command.c_str());
        remove("../game_file.txt.");
        exit(0);
    }

    string message = "This is a racing simulation";
    glColor3f(0, 0, 0);
    glRasterPos2i(0, 20);
    for (char letter : message) {
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, letter);
    }

    string message2 = "Note however, this will not affect the results, but will show how the winner is determined";
    glColor3f(0, 0, 0);
    glRasterPos2i(0, 40);
    for (char letter : message2) {
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, letter);
    }

    string message3 = "To move, press the left arrow, hold it for maximum speed";
    glColor3f(0, 0, 0);
    glRasterPos2i(0, 60);
    for (char letter : message3) {
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, letter);
    }

    string message4 = "Once you or the opponent hit the end of the window, the simulation ends";
    glColor3f(0, 0, 0);
    glRasterPos2i(0, 80);
    for (char letter : message4) {
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, letter);
    }

    glFlush();  // Render now
}

// http://www.theasciicode.com.ar/ascii-control-characters/escape-ascii-code-27.html
void kbd(unsigned char key, int x, int y) {
    // escape
    if (key == 27) {
        glutDestroyWindow(wd);
        cout << "\nEnding Simulation" << endl;
        string command;
        command =  python + " ../game_ending.py ";
        system(command.c_str());
        remove("../game_file.txt.");
        exit(0);
    }

    glutPostRedisplay();
}

void kbdS(int key, int x, int y) {
    switch(key) {
        case GLUT_KEY_DOWN:
            break;
        case GLUT_KEY_LEFT:
            break;
        case GLUT_KEY_RIGHT:
            for (unique_ptr<Shape> &u: user) {
                u->moveX(4);
            }
            break;
        case GLUT_KEY_UP:
            break;
    }

    glutPostRedisplay();
}

void cursor(int x, int y) {
    glutPostRedisplay();
}

// button will be GLUT_LEFT_BUTTON or GLUT_RIGHT_BUTTON
// state will be GLUT_UP or GLUT_DOWN
void mouse(int button, int state, int x, int y) {

    glutPostRedisplay();
}

void userTimer(int dummy) {
    for (unique_ptr<Shape> &u : user) {
        u->moveX(-1);
    }
    glutPostRedisplay();
    glutTimerFunc(50, userTimer, dummy);
}

void opponentTimer(int dummy) {
    for (unique_ptr<Shape> &o : opponent) {
        o->moveX(4);
        // If a shape has moved off the screen...
    }

    glutPostRedisplay();
    glutTimerFunc(50, opponentTimer, dummy);
}

void lineTimer(int dummy) {
    for (int i = 0; i < yellowLine.size(); ++i) {
        yellowLine[i].moveX(-3);
        if (yellowLine[i].getLeftX() < -(yellowLine[i].getWidth()/2)) {
            yellowLine[i].setCenterX(width);
        }
    }
    glutPostRedisplay();
    glutTimerFunc(50, lineTimer, dummy);
}

void cloudTimer(int dummy) {
    for (unique_ptr<Shape> &s : clouds) {
        s->moveX(-3);
        if (s->getCenterX() < -20) {
            s->setCenterX(width+10);
        }
    }
    glutPostRedisplay();
    glutTimerFunc(50, cloudTimer, dummy);
}

/* Main function: GLUT runs as a console application starting at main()  */
int main(int argc, char** argv) {

    starter();
    if (ifstream ("../game_file.txt.")){
        init();

        glutInit(&argc, argv);          // Initialize GLUT

        glutInitDisplayMode(GLUT_RGBA);

        glutInitWindowSize((int) width, (int) height);
        glutInitWindowPosition(100, 200); // Position the window's initial top-left corner
        /* create the window and store the handle to it */
        wd = glutCreateWindow("Race Simulation" /* title */ );

        // Register callback handler for window re-paint event
        glutDisplayFunc(display);

        // Our own OpenGL initialization
        initGL();

        // register keyboard press event processing function
        // works for numbers, letters, spacebar, etc.
        glutKeyboardFunc(kbd);

        // register special event: function keys, arrows, etc.
        glutSpecialFunc(kbdS);

        // handles mouse movement
        glutPassiveMotionFunc(cursor);

        // handles mouse click
        glutMouseFunc(mouse);

        // handles timer
        glutTimerFunc(0, cloudTimer, 0);
        glutTimerFunc(0, userTimer, 0);
        glutTimerFunc(0, opponentTimer, 0);
        glutTimerFunc(0,lineTimer,0);

        // Enter the event-processing loop
        glutMainLoop();
    }
    return 0;
}

