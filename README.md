# ZombieBot
Content Bot for wykop.pl (tags bitcoin, kryptowaluty)

Dokumentacja :) w pliku
https://github.com/a000b/ZombieBot/blob/master/dokumentacja.png

W pliku https://github.com/a000b/ZombieBot/blob/master/auth_wykop_struct.json
przechowywane są dane do logowania usrkey nie jest przechowywany jest odnawiany przy każdym użyciu. Zrobiłem tak, bo nie chciało mi się pisać obsługi sprawdzania czy jest jeszcze ważny, choć w sumie powinna być.

Plik bakkt_stats.csv to na szybko próba zachowania statystyk dziennych wolumenu. Może do późniejszego wykresu.

Nie jest wskazane żeby łączyć programy w jeden plik, ponieważ są one uruchamiane jako joby na serwerze, a chcę żeby wpisy dodawały się w różych dniach o różych porach. 


