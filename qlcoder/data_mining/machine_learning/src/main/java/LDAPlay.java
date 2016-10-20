import LDA.Corpus;
import LDA.LdaGibbsSampler;
import LDA.LdaUtil;

import java.io.IOException;
import java.util.Map;

/**
 * Created by cheyulin on 10/20/16.
 */
public class LDAPlay {
    public static void main(String[] args) throws IOException {
        // 1. Load corpus from disk
        Corpus corpus = Corpus.load("data/topic_model_texts");
        // 2. Create a LDA sampler
        LdaGibbsSampler ldaGibbsSampler = new LdaGibbsSampler(corpus.getDocument(), corpus.getVocabularySize());
        // 3. Train it
        ldaGibbsSampler.gibbs(8);
        // 4. The phi matrix is a LDA model, you can use LdaUtil to explain it.
        double[][] phi = ldaGibbsSampler.getPhi();
        Map<String, Double>[] topicMap = LdaUtil.translate(phi, corpus.getVocabulary(), 8);
        LdaUtil.explain(topicMap);
    }
}
