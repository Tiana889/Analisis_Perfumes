# Crear una función que devuelva los perfumes más similares
def get_similar_perfumes(perfume_index, num_recommendations=5):
    # Obtener las similitudes para el perfume seleccionado
    sim_scores = list(enumerate(cosine_sim[perfume_index]))
    
    # Ordenar los perfumes por similitud
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Obtener los índices de los perfumes más similares
    sim_scores = sim_scores[1:num_recommendations+1]
    perfume_indices = [i[0] for i in sim_scores]
    
    # Devolver los nombres y marcas de los perfumes recomendados
    return df2[['Name', 'Brand',  'Notes']].iloc[perfume_indices]