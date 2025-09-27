def normalize_results(results):
    return [res.dict() for res in results]

def resolve_entities(normalized):
    entities = {}
    for res in normalized:
        value = res.get('snippet', '')  
        if '@' in value:
            entity_type = 'email'
        else:
            entity_type = 'unknown'
        if value not in entities:
            entities[value] = {'type': entity_type, 'results': []}
        entities[value]['results'].append(res)
    return entities
