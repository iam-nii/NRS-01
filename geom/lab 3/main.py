import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

vertices = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
faces = [(0, 2, 4), (0, 4, 3), (0, 3, 5), (0, 5, 2), (1, 2, 4), (1, 4, 3), (1, 3, 5), (1, 5, 2)]

camera_x, camera_y, camera_z = 0, 0, 5

def initGL():
    glClearColor(0, 0, 0, 1)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, (0, 0, 5, 1))

def drawOctahedron():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(camera_x, camera_y, camera_z, 0, 0, 0, 0, 1, 0)

    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
    glMaterialfv(GL_FRONT, GL_SPECULAR, [1, 1, 1, 1])
    glMaterialfv(GL_FRONT, GL_SHININESS, [50])
    glMaterialfv(GL_FRONT, GL_EMISSION, [0, 0, 0, 1])

    for face in faces:
        glBegin(GL_POLYGON)
        for vert in face:
            glColor3f(1, 1, 1)
            glVertex3fv(vertices[vert])
        glEnd()

    glutSwapBuffers()

def specialKeys(key, x, y):
    global camera_x, camera_y, camera_z
    step = 0.1

    if key == GLUT_KEY_LEFT:
        camera_x -= step
    elif key == GLUT_KEY_RIGHT:
        camera_x += step
    elif key == GLUT_KEY_UP:
        camera_z -= step
    elif key == GLUT_KEY_DOWN:
        camera_z += step

    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Octahedron with Camera Control")

    glutDisplayFunc(drawOctahedron)
    glutSpecialFunc(specialKeys)

    initGL()
    glutMainLoop()

if __name__ == "__main__":
    main()