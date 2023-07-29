//
// Created by Phileosin on 2023/7/29.
// This is a convertor converting a txt file into data.csv
#include <iostream>
#include <fstream>
#include <sstream>

int main() {
    std::string filename;
    std::cout << "Enter txt file name to convert into csv file: ";
    std::cin >> filename;

    std::ifstream file(filename);
    if (!file) {
        std::cerr << "Error opening file: " << filename << std::endl;
        return 1;
    }

    std::ofstream outfile("data.csv");
    if (!outfile) {
        std::cerr << "Error creating output file" << std::endl;
        return 1;
    }

    // Output the CSV header
    outfile << "Timestamp,Key" << std::endl;

    std::string line;
    while (std::getline(file, line, '\n')) {
        std::istringstream iss(line);
        long double timestamp;
        std::string key;
        char comma;

        if (!(iss >> timestamp >> comma >> key)) {
            std::cerr << "Error reading line: " << line << std::endl;
            continue;
        }

        // Output the data directly to the target CSV file
        outfile << timestamp << "," << key << std::endl;
    }

    file.close();
    outfile.close();

    std::cout << "Data has been saved to data.csv!" << std::endl;

    return 0;
}
