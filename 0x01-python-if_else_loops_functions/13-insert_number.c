#include <stdlib.h>
#include "lists.h"
/**
*insert_node - inserts node into a list
*@head: a pointer to the head of a linked list
*@number: number to insert
*Return: NULL if it fails or a pointer to the new node
*/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node = *head;
listint_t *temp_node;

temp_node = malloc(sizeof(listint_t));
if (temp_node == NULL)
return (NULL);
temp_node->n = number;
if (new_node->n >= number || new_node == NULL)
{
temp_node->next = new_node;
*head = temp_node;
return (temp_node);
}
while (new_node->next && new_node && new_node->next->n < number)
new_node = new_node->next;
temp_node->next = new_node->next;
new_node->next = temp_node;

return (temp_node);
}
