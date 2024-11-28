
# Cypher Query Examples

This document contains examples of Cypher queries for working with nodes and relationships in a Neo4j graph database.

---

## **1. Creating a Node**

```cypher
CREATE (n:Person {name: "Alice", age: 30})
RETURN n
```
- **Explanation:** Creates a node with the label `Person` and properties `name` and `age`.

---

## **2. Creating a Relationship**

```cypher
MATCH (a:Person {name: "Alice"}), (b:Person {name: "Bob"})
CREATE (a)-[:FRIEND]->(b)
RETURN a, b
```
- **Explanation:** Creates a relationship of type `FRIEND` between two nodes, `Alice` and `Bob`.

---

## **3. Deleting a Relationship**

```cypher
MATCH (a:Person {name: "Alice"})-[r:FRIEND]->(b:Person {name: "Bob"})
DELETE r
```
- **Explanation:** Deletes the `FRIEND` relationship between `Alice` and `Bob`.

---

## **4. Transferring a Relationship from One Node to Another**

```cypher
MATCH (a:Person {name: "Alice"})-[r:FRIEND]->(b:Person {name: "Bob"}), 
      (c:Person {name: "Charlie"})
CREATE (c)-[:FRIEND]->(b)
DELETE r
RETURN c, b
```
- **Explanation:** Transfers the `FRIEND` relationship from `Alice` to `Charlie`.

---

## **5. Finding Circular Relationships**

```cypher
MATCH p=(n)-[*]->(n)
RETURN p
```
- **Explanation:** Finds all paths that start and end at the same node (cycles).

---

## Notes
- Ensure your graph database is running before executing these queries.
- Adapt the queries based on your graph's schema or specific requirements.
