#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * 
 * 
 * 
 * 
*/

void vowel(char *passsword)
{
	int i = 0, j = 0, added = 0, total_string = 0;
	char *Vpassword = NULL;
	char array[] = {'a', 'e', 'i', 'o', 'u'};

	added = strlen(passsword) / 2;
	total_string = added + strlen(passsword);
	Vpassword = malloc(sizeof(char) * (total_string + 1));
	for (j = 0; j < total_string; j++)
	{
		if (i % 2 != 0)
		{
			printf("%d\n", i);
			Vpassword[j] = array[3];
			j++;
		}

		Vpassword[j] = passsword[i];
		i++; 
	}
	Vpassword[j] = '\0';

	printf("%s  lenght %ld\n", Vpassword, strlen(Vpassword));

	free(Vpassword);
}

/**
 * 
 * 
 * 
 * 
 * 
*/
char *devowel(char **password)
{
	int i = 0, j = 0;
	char *DVpassword = NULL;

	DVpassword = malloc(sizeof(char) * (strlen(*password) + 1));
	for (j = 0; j < strlen(*password); j++)
	{
		if ( i % 2 == 0 && i % 3 == 0)
			i++;
		
		DVpassword[j] = (*password)[i];
		i++;
	}
	DVpassword[j] = '\0';
	printf("%s\n", DVpassword);
	return (DVpassword);
}


/**
 * 
 * 
 * 
 * 
*/
void encrypt(char *password)
{
	int i;
	char *enpas = NULL;

	printf("Encrypting\n");
	enpas = malloc(sizeof(char) * (strlen(password) + 1));
	if (!enpas)
		return;
	for (i = 0; i < strlen(password); i++)
	{
		printf("%c\n", password[i]);
		enpas[i] = password[i] + 5;
	}
	enpas[i] = '\0';
	printf("%s\n", enpas);
	vowel(enpas);
	free(enpas);
}

/**
 * 
 * 
 * 
 * 
*/
void decrypt(char *password)
{
	int i;
	char *enpas = NULL;

	printf("Decrypting\n");
	devowel(&password);
	// for (i = 0; i < strlen(password); i++)
	// 	enpas[i] = password[i] - 5;
	// enpas[i] = '\0';
	// printf("%s\n", enpas);

}

/**
 *
 *
 *
 *
 */
void *parameter_selector(char *arg, char *password)
{
	int i;

	for (i = 0; i < 2; i++)
	{
		if (!strncmp(arg, "--e", 3))
		{
			encrypt(password);
			return (NULL);
		}
		else if (!strncmp(arg, "--r", 3))
		{
			printf("%s\n", password);
			decrypt(password);
			return (NULL);
		}
		
	}
	
}


/**
 *
 *
 *
 *
 */

int main(int argc, char *argv[])
{
	char *parameters[2];

	if (argc == 1)
	{
		fprintf(stderr, "<Usage> is %s, parameters {--r :'reverse'} and {--e: 'encrypt'}  <password> e.g 'name@2'\n", argv[0]);
		return (-1);
	}
	parameters[0] = "--r";
	parameters[1] = "--e";

	if (argv[1] && argv[2])
	{
		if (strncmp(argv[1], parameters[0], 3) == 0 || strncmp(argv[1], parameters[1], 3) == 0)
		{
			if (strlen(argv[2]) >= 4)
				parameter_selector(argv[1], argv[2]);
			else
				fprintf(stderr, "password lenght must greater that four\n");
		}
		else
		{
			fprintf(stderr, "parameter %s not found, Use {--r :'reverse'} and {--e: 'encrypt'}\n", argv[1]);
			return (-1);
		}

	}
	else
	{
		fprintf(stderr, "password is missing");
		return (-1);

	}
}