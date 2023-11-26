#include<stdio.h>
#include<string.h>
#include<stdlib.h>

struct Produto {
  char nome[100];
  int codigo;
  double preco;
};

typedef struct node {
  struct Produto produto;
  struct node *next;
} Node;

///////////////////////////////////////////////////////////////////////////////////////////////////////////////

Node *create_node(){
  Node *ptr = malloc(sizeof(*ptr));
  if(!ptr){
    printf("\t** Erro ao alocar memoria **\n");
    exit(1);
  }
  else{
    return ptr;
  }
}

Node *insert_node(Node *lista, char *nome, int codigo, double preco){
  Node *insert_node = create_node();
  strcpy(insert_node->produto.nome, nome);
  insert_node->produto.codigo = codigo;
  insert_node->produto.preco = preco;
  if( lista == NULL){
    lista = insert_node;
    insert_node->next = NULL;
  }
  else{
    Node *busca = lista;
    while(busca->next != NULL){
      busca = busca->next;
    }
    busca->next = insert_node;
    insert_node->next = NULL;
  }
  return lista;
}

Node *insert_node_order(Node *lista, char *nome, int codigo, double preco){
  Node *insert_node = create_node();
  strcpy(insert_node->produto.nome, nome);
  insert_node->produto.codigo = codigo;
  insert_node->produto.preco = preco;
  if( lista == NULL){
    lista = insert_node;
    insert_node->next = NULL;
  }
  else{
    Node *busca = lista;
    while(busca->next != NULL){
      busca = busca->next;
    }
    Node *temp = NULL;
    if(insert_node->produto.codigo > busca->produto.codigo){
      if(busca->next != NULL){
        temp = busca->next;
        busca->next = insert_node;
        insert_node->next = temp;
        temp->next = NULL;
      }
    }
    else{
      if(busca->next != NULL){
        temp = busca->next;
        insert_node->next = busca;
        busca->next = temp;
        lista = insert_node;
      }
      else{
        insert_node->next = busca;
        busca->next = NULL;
        lista = insert_node;
      }
    }
  }
  return lista;
}


Node *delete_nodes(Node *lista){
  Node *temp = NULL;
  while(lista != NULL){
    temp = lista->next;
    free(lista);
    lista = temp;
  }
  return lista;
}

void show_list(Node *lista){
  Node *temp = NULL;
  temp = lista;
  while(temp != NULL){
    printf("\n\tNome: %s \tCodigo: %d \tPreco: %.2lf\n", temp->produto.nome, temp->produto.codigo, temp->produto.preco);
    temp = temp->next;
  }
}

void search_node(Node *lista, char *nome){
  Node *temp = NULL;
  temp = lista;
  while(temp != NULL){
    if(!strcmp(temp->produto.nome, nome)){
      printf("\n\tNome: %s \tCodigo: %d \tPreco: %.2lf\n", temp->produto.nome, temp->produto.codigo, temp->produto.preco);
      return;
    }
    temp = temp->next;
  }
  if(temp == NULL){
    printf("\n\t** Produto nao encontrado **\n");
  }
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////

int main(void){
  Node *lista = NULL;
  char nome[50];
  int codigo;
  double preco;
  int res;
  while(res != 4){
    printf("\n1: Inserir um produto\n");
    printf("2: Exibir todos\n");
    printf("3: Buscar produto\n");
    printf("4: Sair\n");
    do{
      printf("Selecione uma opcao: ");
      scanf("%d", &res);
    } while(res < 1 || res > 4);
    getchar();
    switch(res){
      case 1:
        printf("\nInforme o nome: ");
        fgets(nome, sizeof(nome), stdin);
        nome[strcspn(nome, "\n")] = 0;
        printf("Informe o codigo: ");
        scanf("%d", &codigo);
        printf("Informe o preco: ");
        scanf("%lf", &preco);
        lista = insert_node(lista, nome, codigo, preco);
        printf("\n\t** Produto Registrado **\n");
        break;
      case 2:
        if(lista == NULL){
          printf("\n\t** Lista vazia **\n");
          break;
        }
        show_list(lista);
        break;
      case 3:
        if(lista == NULL){
          printf("\n\t** Lista vazia **\n");
          break;
        }
        printf("\nInforme o nome: ");
        fgets(nome, sizeof(nome), stdin);
        nome[strcspn(nome, "\n")] = 0;
        search_node(lista, nome);
        break;
      case 4:
        lista = delete_nodes(lista);
        printf("\nApagando produtos... \n\t** Memoria liberada **\nSaindo...\n");
        break;
      default:
        printf("** Opcao invalida **");
        break;
    }
  }
  return 0;
}
