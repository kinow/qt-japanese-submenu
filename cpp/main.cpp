#include <QDebug>
#include <QApplication>
#include <QtWidgets>
#include <QLabel>
#include <QLineEdit>
#include <QPushButton>
#include <QMenu>
#include <QWidgetAction>
#include <QHBoxLayout>
#include <QVBoxLayout>


int main(int argc, char *argv[])
{
    qDebug() << "Creating application...";
    QApplication a(argc, argv);
    // window...
    QWidget* window = new QWidget();

    // a label
    QLabel* label1 = new QLabel();
    label1->setText("Enter your text");
    // an input field to test (should work)
    QLineEdit* input1 = new QLineEdit();

    // a button
    QPushButton* button1 = new QPushButton();
    // popup menu to add to the button...
    QMenu* popup = new QMenu(window);
    QMenu* submenu = popup->addMenu("ASSIGN?");

    // **the bug must be somewhere in here...**
    {
        // item for the popup menu
        QWidget* widget = new QWidget();

        QHBoxLayout* layout = new QHBoxLayout();

        QLabel* label = new QLabel();
        layout->addWidget(label);

        // maybe this input is not linked to the main application, which has the locale?
        QLineEdit* input = new QLineEdit();
        input->setPlaceholderText("New tag");
        layout->addWidget(input);
        widget->setLayout(layout);

        QWidgetAction* action = new QWidgetAction(popup);
        action->setDefaultWidget(widget);

        submenu->addAction(action);

        button1->setMenu(popup);
    }

    // rest of the UI

    QHBoxLayout* hbox = new QHBoxLayout();
    hbox->addWidget(label1);
    hbox->addWidget(input1);

    QVBoxLayout* vbox = new QVBoxLayout();
    vbox->addLayout(hbox);
    vbox->addWidget(button1);

    window->setLayout(vbox);

    window->resize(530, 140);
    window->move(300, 300);
    window->setWindowTitle("Simple");
    window->show();
    return a.exec();
}

