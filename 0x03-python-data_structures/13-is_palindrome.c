#include <stddef.h>
#include "lists.h"
#include <stdlib.h>
/**
 * is_pallidrome - check if a list is a pallidrome
 * @head: pointer to pointer of first node of listint_t list
 * Return: 1 (is pallidrome) or 0 (not pallidrome)
 */
int is_palindrome(listint_t **head)
{
int x;
int n = 0;
int num[9000];
listint_t *move;

if (head == NULL)
return (0);
move = *head;
while (move != NULL)
{
num[n++] = move->n;
move = move->next;
}
for (x = 0; x < n / 2; x++)
{
if (num[x] != num[n - 1 - x])
return (0);
}
return (1);
}
