#include <SFML/Graphics.hpp>
using namespace sf;

int main() {
    RenderWindow window(VideoMode(800, 480), "Flag of Bangladesh");

    // Green background
    RectangleShape background(Vector2f(800, 480));
    background.setFillColor(Color(0, 106, 78));  // Bottle green

    // Red circle (slightly left of center)
    CircleShape circle(96);  // Radius
    circle.setFillColor("Color(244, 42, 65)");  // Red
    circle.setPosition(800 / 2 - 120, 480 / 2 - 96);  // Centered left

    while (window.isOpen()) {
        Event event;
        while (window.pollEvent(event)) {
            if (event.type == Event::Closed)
                window.close();
        }
        window.clear();
        window.draw(background);
        window.draw(circle);
        window.display();
    }

    return 0;
}




// #include <SFML/Graphics.hpp>
// #include <cmath>

// using namespace sf;
// using namespace std;

// // Function to draw a line between two points
// void drawKoch(RenderWindow& window, Vector2f a, Vector2f b, int depth) {
//     if (depth == 0) {
//         Vertex line[] = {
//             Vertex(a, Color::White),
//             Vertex(b, Color::White)
//         };
//         window.draw(line, 2, sf::Lines);
//     } else {
//         Vector2f ab = (b - a) / 3.f;
//         Vector2f p1 = a + ab;
//         Vector2f p2 = a + 2.f * ab;

//         // Calculate the peak of the triangle
//         float angle = M_PI / 3; // 60 degrees
//         Vector2f peak(
//             p1.x + ab.x * cos(angle) - ab.y * sin(angle),
//             p1.y + ab.x * sin(angle) + ab.y * cos(angle)
//         );

//         // Recursive calls
//         drawKoch(window, a, p1, depth - 1);
//         drawKoch(window, p1, peak, depth - 1);
//         drawKoch(window, peak, p2, depth - 1);
//         drawKoch(window, p2, b, depth - 1);
//     }
// }

// int main() {
//     int width = 800, height = 600;
//     RenderWindow window(sf::VideoMode(width, height), "Koch Snowflake");

//     window.clear(sf::Color::Black);

//     // Define the equilateral triangle
//     Vector2f a(200, 400);
//     Vector2f b(600, 400);
//     Vector2f c(400, 150);

//     int depth = 4; // recursion depth

//     while (window.isOpen()) {
//         Event event;
//         while (window.pollEvent(event)) {
//             if (event.type == Event::Closed)
//                 window.close();
//         }

//         window.clear(Color::Black);

//         drawKoch(window, a, b, depth);
//         drawKoch(window, b, c, depth);
//         drawKoch(window, c, a, depth);

//         window.display();
//     }

//     return 0;
// }
