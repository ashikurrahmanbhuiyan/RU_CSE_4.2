// implement using z buffer

#include <GL/glut.h>

void init() {
    glClearColor(0.0, 0.0, 0.0, 1.0);   // Background color
    glEnable(GL_DEPTH_TEST);           // Enable Z-buffer (depth test)
}

void display() {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT); // Clear color & depth

    glLoadIdentity();
    gluLookAt(0.0, 0.0, 5.0,  // Camera position
              0.0, 0.0, 0.0,  // Look-at point
              0.0, 1.0, 0.0); // Up vector

    // First polygon (red) — farther away
    glColor3f(1.0, 0.0, 0.0);
    glBegin(GL_POLYGON);
        glVertex3f(-0.5, -0.5, -2.0);
        glVertex3f( 0.5, -0.5, -2.0);
        glVertex3f( 0.5,  0.5, -2.0);
        glVertex3f(-0.5,  0.5, -2.0);
    glEnd();

    // Second polygon (green) — closer, overlaps first
    glColor3f(0.0, 1.0, 0.0);
    glBegin(GL_POLYGON);
        glVertex3f(-0.2, -0.2, -1.0);
        glVertex3f( 0.8, -0.2, -1.0);
        glVertex3f( 0.8,  0.8, -1.0);
        glVertex3f(-0.2,  0.8, -1.0);
    glEnd();

    glutSwapBuffers();
}

void reshape(int w, int h) {
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(60.0, (float)w/h, 1.0, 10.0);
    glMatrixMode(GL_MODELVIEW);
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH); // Depth buffer enabled
    glutInitWindowSize(800, 600);
    glutCreateWindow("Z-buffer Hidden Surface Removal");

    init();
    glutDisplayFunc(display);
    glutReshapeFunc(reshape);
    glutMainLoop();
    return 0;
}


/* Run in the terminal
    cd Graphics
    g++ 1.surface_show_hide.cpp -o output -lGL -lGLU -lglut
    ./output
 */