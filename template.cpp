#include <iostream>
#include <string>

std::string MacCompony(const int macDigit){
	switch (macDigit){
		// ***insert_point***
		case 123: return "good";
		// ***insert_point***
		default: return "unknown";
	}
	return "unknown";
}

int main(int argc, char* argv[]) {
	for (int i = 1; i < argc; ++i) {
		const std::string mac = std::string(argv[i]);
		int macDigit = 0;
		int addTimes = 0;
		for(char c: mac){
			if (isalnum(c)) {
				c = toupper(c);
				if (c >= 'A' && c <= 'F') {
					macDigit = macDigit * 16 + 10 + c - 'A';
				}
				else {
					macDigit = macDigit * 16 + c - '0';
				}
				addTimes++;
				if (addTimes >= 6) {
					break;
				}
			}
		}
		const std::string ans = MacCompony(macDigit);
		std::cout << mac << " " << ans << std::endl;
	}
	return 0;
}
