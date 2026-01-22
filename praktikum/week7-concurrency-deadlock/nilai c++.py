#include <iostream>
using namespace std; 
// Library untuk input-output.

int main() {
    int nilai;
    cout << "Masukkan nilai mahasiswa: ";
    cin >> nilai;
    // Meminta pengguna memasukkan nilai.

    if (nilai >= 85) {
        cout << "Nilai A";
        // Jika nilai ≥ 85 → A
    } else if (nilai >= 75) {
        cout << "Nilai B";
        // Jika nilai 75–84 → B
    } else if (nilai >= 60) {
        cout << "Nilai C";
        // Jika nilai 60–74 → C
    } else {
        cout << "Nilai D";
        // Di bawah 60 → D
    }

    return 0; 
    // Program selesai.
}
