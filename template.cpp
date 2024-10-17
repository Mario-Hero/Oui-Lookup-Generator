#include <iostream>
#include <unordered_map>
#include <string>

int main(int argc, char* argv[]) {
	// ***insert_point***
	std::unordered_map<int, std::string> oui_data = {
		{1108370,"INGRAM MICRO SERVICES"}
	};
	// ***insert_point***
	for (int i = 1; i < argc; ++i) {
		const std::string mac = std::string(argv[i]);
		int mac_digit = 0;
		int addTimes = 0;
		for(char c: mac){
			if (isalnum(c)) {
				c = toupper(c);
				if (c >= 'A' && c <= 'F') {
					mac_digit = mac_digit * 16 + 10 + c - 'A';
				}
				else {
					mac_digit = mac_digit * 16 + c - '0';
				}
				addTimes++;
				if (addTimes >= 6) {
					break;
				}
			}
		}
		
		const auto it = oui_data.find(mac_digit);
		if (it != oui_data.end()) {
			std::cout << mac << " " << it->second << std::endl;
		}
		else {
			std::cout << mac << " unknown" << std::endl;
		}
	}
	return 0;
}