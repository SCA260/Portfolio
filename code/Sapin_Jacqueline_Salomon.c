#include <stdio.h>
// pour utiliser random
#include <stdlib.h>
// pour les couleurs
#define KRED  "\x1B[31m"    /* Red */
#define KGRN  "\x1B[32m"    /* Green */
#define KYEL  "\x1B[33m"    /* Yellow */
#define KWHI  "\x1B[37m"    /* White */
#define RESET "\033[0m"

//La décoration
// char decorations[][4] = { KRED "0" RESET,KYEL "$" RESET,KWHI "@" RESET,KYEL "&" RESET,KRED "+" RESET};
//Triangle du sapin
void etage(int taille,int nbetage) //nbetage = 0 initialement et augmentera à chaque fois qu'elle sera appelé
{
    int ligne = 4 + nbetage;
    int nbmax = 7+8*(taille-1); //7 : nb car max sur 1 ligne | 8 : le plus grand écart possible pour éviter que + c'est grand, + ça se déforme
    // sur la gauche à cause de la taille du terminal (10 étages max)
    int nbstar = (nbetage==0)? 1 : 1+2*(ligne-3)+4*(nbetage-1); //utilisation du ternaire pour vérif
    // si c'est le 1er étage ou autre, si c'est le cas = va afficher 1 à 7 étoiles, sinon, prends 2 lignes en - pour comencer le prochain étage
    while(ligne> 0){
        for(int i=0; i < nbmax/2 - nbstar/2 ; i++){
            printf(" "); //affiche un espace via le putchar qui est l'équivalent d'un printf mais pour 1caractère
        }
        for (int i=0; i < nbstar; ++i) {
            printf(KGRN "*" RESET);
        }
        printf("\n");
        nbstar+=2;
        ligne--;
    }
}

//tronc du sapin
void tronc(int taille)
{
    int nbmax = 7+8*(taille-1);//Taille de l'espacement

    for (int j = 0; j < taille; j++)
    {
        for (int k = 0; k < nbmax/2-taille/2; k++) //va de 0 à la taille par pas de 1
        {
            printf(" ");
        }

        char base_tronc = 124;

        for (int k = 0; k < taille; k++)
        {
            printf(KRED "%c" RESET, base_tronc);
        }
        printf("\n");

    }
}

int main(){
    int demo;
    int taille;
    char numberRead[20];
    printf(" Voulez vous voir une Demo ? \n 1 = Oui \t Autre touche = Non \n");
    scanf("%i",&demo);
    // utilisation du switch pour la demo
        switch (demo)
        {
        case 1:
            for (int d = 0; d <= 5; d++)
            {
                {
                    taille = d;
                    for (int h = 0; h < taille; ++h){
                        printf("\n");
                        etage(taille, h);
                    }
                    tronc(taille);
                    printf("\n");
                    printf("demo pour la taille : %i \n", taille);
                }
            }
            break;
        default:
            do
            {
                printf("Veuillez entrer la taille du tronc du " KGRN "sapin " RESET ":\n");
                scanf("%s", numberRead);
                taille = atoi(numberRead);
                printf(" ce n'est pas un nombre \n");

            } while (taille < 1);
            printf("vous avez entr%c %d\n",130,taille);
            putchar('\n');
            for (int i = 0; i < taille; ++i){
                etage(taille, i);
            }
            tronc(taille);
            break;
        }
    return 0;
}