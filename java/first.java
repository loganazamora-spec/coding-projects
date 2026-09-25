void main() {

    IO.println("Hello, world!");

    int age;

    age = 18;

    String age_declaration = "I am " + age + " years old.";

    IO.println(age_declaration);
    
    secondLine();
    data_cast();
}



void secondLine() {
    IO.print("This is the second line. ");

    IO.println("As in: " + 2);
}

void data_cast() {
    double avg_class_age = (16+18+18+16+19+18+17+16+18)/9.0;

    IO.println("Average class age: " + String.format("%.2f", avg_class_age));

    IO.print("But, more cleanly: ");

    IO.println((int) avg_class_age);

} 

