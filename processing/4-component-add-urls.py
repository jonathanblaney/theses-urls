import re
from creategrep1 import infile
from creategrep1 import finaloutfile

f = open(infile, 'r')
text = f.read()
f.close()

text = re.sub(r'(?i)(Milton.?s History of Britain [^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.236197">\\1</a>', text)
text = re.sub(r'(?i)(The lives of the early Irish[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.238586">\\1</a>', text)
text = re.sub(r'(?i)(The social and ecclesiastica[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.239387">\\1</a>', text)
text = re.sub(r'(?i)(Alcibiades and Athens ?. a st[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.239401">\\1</a>', text)
text = re.sub(r'(?i)(Matthew Paris and Anglo-Saxo[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.241317">\\1</a>', text)
text = re.sub(r'(?i)(The Roman Alexander ?. studie[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.242539">\\1</a>', text)
text = re.sub(r'(?i)(A commentary on Quintus Curt[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.243234">\\1</a>', text)
text = re.sub(r'(?i)(A commentary on Q. Curtius R[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.243274">\\1</a>', text)
text = re.sub(r'(?i)(A post-conquest English retr[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.245904">\\1</a>', text)
text = re.sub(r'(?i)(Sir John Hayward and early S[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.246357">\\1</a>', text)
text = re.sub(r'(?i)(Newspapers and historical re[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.248842">\\1</a>', text)
text = re.sub(r'(?i)(The origin of the Turks ?. a [^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.249346">\\1</a>', text)
text = re.sub(r'(?i)(The life of S. Pancratius of[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.249853">\\1</a>', text)
text = re.sub(r'(?i)(John Venn.?s Alumni Cantabrig[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.251421">\\1</a>', text)
text = re.sub(r'(?i)(Justin Martyr ?. a theology o[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.255223">\\1</a>', text)
text = re.sub(r'(?i)(Byzantine historiography in [^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.255806">\\1</a>', text)
text = re.sub(r'(?i)(Poverty and the historians ?.[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.256144">\\1</a>', text)
text = re.sub(r'(?i)(Determinism in humanist hist[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.258649">\\1</a>', text)
text = re.sub(r'(?i)(Quintus Curtius Rufus.? .?Hist[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.260613">\\1</a>', text)
text = re.sub(r'(?i)(A translation and historical[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.261430">\\1</a>', text)
text = re.sub(r'(?i)(Representations of the Secon[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.264327">\\1</a>', text)
text = re.sub(r'(?i)(Plotting Irish history ?. nat[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.267601">\\1</a>', text)
text = re.sub(r'(?i)(Subjects of history ?. the pr[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.267988">\\1</a>', text)
text = re.sub(r'(?i)(The influence of Switzerland[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.268257">\\1</a>', text)
text = re.sub(r'(?i)(Sites of salvage ?. science h[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.275822">\\1</a>', text)
text = re.sub(r'(?i)(The Presbyterian interpretat[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.275939">\\1</a>', text)
text = re.sub(r'(?i)(William Harrison \(1535-1593\)[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.279489">\\1</a>', text)
text = re.sub(r'(?i)(The historiography of Henry [^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.280203">\\1</a>', text)
text = re.sub(r'(?i)(Dionysius of Halicarnassus a[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.281092">\\1</a>', text)
text = re.sub(r'(?i)(Idealist and pragmatist elem[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.281782">\\1</a>', text)
text = re.sub(r'(?i)(Mao and history ?. an interpr[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.283849">\\1</a>', text)
text = re.sub(r'(?i)(The texts ?. transmission and [^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.284201">\\1</a>', text)
text = re.sub(r'(?i)(Medical biography and autobi[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.284246">\\1</a>', text)
text = re.sub(r'(?i)(Reforming Rome ?. the recepti[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.285479">\\1</a>', text)
text = re.sub(r'(?i)(The historical thought of S.[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.285605">\\1</a>', text)
text = re.sub(r'(?i)(Writing Wounded Knee ?. repre[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.285982">\\1</a>', text)
text = re.sub(r'(?i)(Politics and identity ?. a cr[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.286283">\\1</a>', text)
text = re.sub(r'(?i)(C. Licinius Macer and the hi[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.286592">\\1</a>', text)
text = re.sub(r'(?i)(.?Nabob ?. historian and orient[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.287778">\\1</a>', text)
text = re.sub(r'(?i)(Hagiography in England in th[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.290814">\\1</a>', text)
text = re.sub(r'(?i)(The Historiae of Theophylact[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.291572">\\1</a>', text)
text = re.sub(r'(?i)(The British debate on the Fr[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.292574">\\1</a>', text)
text = re.sub(r'(?i)(Hydatius ?. a late Roman chro[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.293368">\\1</a>', text)
text = re.sub(r'(?i)(George Grote on Plato and At[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.295669">\\1</a>', text)
text = re.sub(r'(?i)(Izaak Walton and his precurs[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.296659">\\1</a>', text)
text = re.sub(r'(?i)(Art and identity in the Mari[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.300724">\\1</a>', text)
text = re.sub(r'(?i)(Wonders in central medieval [^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.300799">\\1</a>', text)
text = re.sub(r'(?i)(Divination and Roman histori[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.302565">\\1</a>', text)
text = re.sub(r'(?i)(A critical edition of Tarikh[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.304128">\\1</a>', text)
text = re.sub(r'(?i)(An unexploited source for th[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.304773">\\1</a>', text)
text = re.sub(r'(?i)(An historical commentary on [^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.305861">\\1</a>', text)
text = re.sub(r'(?i)(The Historia Iherosolimitana[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.309967">\\1</a>', text)
text = re.sub(r'(?i)(Commemorating the past ?. a c[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.309980">\\1</a>', text)
text = re.sub(r'(?i)(Perceptions of the Thirty Ye[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.310295">\\1</a>', text)
text = re.sub(r'(?i)(Elite perceptions of the Vic[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.311227">\\1</a>', text)
text = re.sub(r'(?i)(Antiquarianism in the Midlan[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.311570">\\1</a>', text)
text = re.sub(r'(?i)(Transforming history ?. women[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.313554">\\1</a>', text)
text = re.sub(r'(?i)(Studies in oral tradition an[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.314263">\\1</a>', text)
text = re.sub(r'(?i)(Authorship and authority in [^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.314546">\\1</a>', text)
text = re.sub(r'(?i)(Ovid and the Fasti ?. an hist[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.314889">\\1</a>', text)
text = re.sub(r'(?i)(The reception of Geoffrey of[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.314984">\\1</a>', text)
text = re.sub(r'(?i)(The Goggam Chronicle ?. intro[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.316806">\\1</a>', text)
text = re.sub(r'(?i)(Scottish Whig historiography[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.317686">\\1</a>', text)
text = re.sub(r'(?i)(John Ruskin.?s understanding [^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.317719">\\1</a>', text)
text = re.sub(r'(?i)(A study of the English lives[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.318199">\\1</a>', text)
text = re.sub(r'(?i)(The Scotorum Historia of Hec[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.320654">\\1</a>', text)
text = re.sub(r'(?i)(Rhetorics and reality ?. the [^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.326655">\\1</a>', text)
text = re.sub(r'(?i)(Byzantine hagiographies in A[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.327547">\\1</a>', text)
text = re.sub(r'(?i)(Plutarch and Rome ?. three st[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.329217">\\1</a>', text)
text = re.sub(r'(?i)(Medieval Irish saints.? lives[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.329273">\\1</a>', text)
text = re.sub(r'(?i)(A study of Ottoman historiog[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.335692">\\1</a>', text)
text = re.sub(r'(?i)(Enlightenment historical wri[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.335741">\\1</a>', text)
text = re.sub(r'(?i)(The ancient ?. famous and hono[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.336252">\\1</a>', text)
text = re.sub(r'(?i)(The unwritten verities of th[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.338251">\\1</a>', text)
text = re.sub(r'(?i)(Vernacular history in the ma[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.339442">\\1</a>', text)
text = re.sub(r'(?i)(The politics of time ?. .?prim[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.341919">\\1</a>', text)
text = re.sub(r'(?i)(Sir James Edmonds and the Of[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.342286">\\1</a>', text)
text = re.sub(r'(?i)(Fictive ancient history and [^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.343420">\\1</a>', text)
text = re.sub(r'(?i)(Change and continuity in Eng[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.347744">\\1</a>', text)
text = re.sub(r'(?i)(The writing of Thomas Carlyl[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.348951">\\1</a>', text)
text = re.sub(r'(?i)(Liberalism and historicism ?.[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.349838">\\1</a>', text)
text = re.sub(r'(?i)(The evolution of the decline[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.349873">\\1</a>', text)
text = re.sub(r'(?i)(William Mitford and Greek hi[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.352280">\\1</a>', text)
text = re.sub(r'(?i)(The historical novel as phil[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.352384">\\1</a>', text)
text = re.sub(r'(?i)(A commentary on Livy Book Ni[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.353680">\\1</a>', text)
text = re.sub(r'(?i)(.?A commentary on Plutarch.?s [^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.354793">\\1</a>', text)
text = re.sub(r'(?i)(The early county historians [^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.357496">\\1</a>', text)
text = re.sub(r'(?i)(Materials towards a critical[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.358427">\\1</a>', text)
text = re.sub(r'(?i)(Giambattista Vico ?. imaginat[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.359696">\\1</a>', text)
text = re.sub(r'(?i)(The writing of urban histori[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.359724">\\1</a>', text)
text = re.sub(r'(?i)(The construction of the Holo[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.361889">\\1</a>', text)
text = re.sub(r'(?i)(History in black and white ?.[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.363761">\\1</a>', text)
text = re.sub(r'(?i)(A critical reconstruction an[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.370632">\\1</a>', text)
text = re.sub(r'(?i)(The legacy of evangelicalism[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.371763">\\1</a>', text)
text = re.sub(r'(?i)(John Lingard ?. The historian[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.372498">\\1</a>', text)
text = re.sub(r'(?i)(The Gesta Dei per Francos of[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.373563">\\1</a>', text)
text = re.sub(r'(?i)(The politics of German histo[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.373895">\\1</a>', text)
text = re.sub(r'(?i)(Agents and masters in ancien[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.374420">\\1</a>', text)
text = re.sub(r'(?i)(A critical edition of volume[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.382923">\\1</a>', text)
text = re.sub(r'(?i)(Arab historians and the rise[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.383066">\\1</a>', text)
text = re.sub(r'(?i)(Economics and modes of secur[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.385482">\\1</a>', text)
text = re.sub(r'(?i)(Golden ages and barbarous na[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.386145">\\1</a>', text)
text = re.sub(r'(?i)(Procopius and the Persian Wa[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.386491">\\1</a>', text)
text = re.sub(r'(?i)(Recent interpretations of hi[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.387086">\\1</a>', text)
text = re.sub(r'(?i)(Writing people into the land[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.390741">\\1</a>', text)
text = re.sub(r'(?i)(Writing the history of the R[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.394263">\\1</a>', text)
text = re.sub(r'(?i)(Tyche ?. fortune and chance i[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.394904">\\1</a>', text)
text = re.sub(r'(?i)(Ammianus Marcellinus ?. autop[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.395223">\\1</a>', text)
text = re.sub(r'(?i)(The Holocaust and the entwin[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.395981">\\1</a>', text)
text = re.sub(r'(?i)(Epigraphical research and hi[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.401889">\\1</a>', text)
text = re.sub(r'(?i)(How Keats read his histories[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.404195">\\1</a>', text)
text = re.sub(r'(?i)(The .?Sibylla Tiburtina.? and [^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.407394">\\1</a>', text)
text = re.sub(r'(?i)(Roman noble self-presentatio[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.410819">\\1</a>', text)
text = re.sub(r'(?i)(Hibernia ?. Celtic tiger in t[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.410987">\\1</a>', text)
text = re.sub(r'(?i)(Factional pasts ?. the shifti[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.414032">\\1</a>', text)
text = re.sub(r'(?i)(Josephus and the Maccabean R[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.414655">\\1</a>', text)
text = re.sub(r'(?i)(Studies on the composition o[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.416030">\\1</a>', text)
text = re.sub(r'(?i)(Kingmaking ?. the historiogra[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.417945">\\1</a>', text)
text = re.sub(r'(?i)(Reginald of Durham and St. G[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.418649">\\1</a>', text)
text = re.sub(r'(?i)(Once called Albion ?. the com[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.418835">\\1</a>', text)
text = re.sub(r'(?i)(Cecil Roth and the imaginati[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.419162">\\1</a>', text)
text = re.sub(r'(?i)(The composition and context [^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.420029">\\1</a>', text)
text = re.sub(r'(?i)(Identifying Romanness ?. virt[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.421720">\\1</a>', text)
text = re.sub(r'(?i)(Argentina.?s partisan past ?. [^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.429165">\\1</a>', text)
text = re.sub(r'(?i)(The representation of women ?.[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.430574">\\1</a>', text)
text = re.sub(r'(?i)(.?A chief standard work.? ?. th[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.431109">\\1</a>', text)
text = re.sub(r'(?i)(The idea of the Roman past i[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.431298">\\1</a>', text)
text = re.sub(r'(?i)(The Pax Romana ?. Britannica a[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.432185">\\1</a>', text)
text = re.sub(r'(?i)(The cultural politics of his[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.433569">\\1</a>', text)
text = re.sub(r'(?i)(Bias and objectivity in the [^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.435509">\\1</a>', text)
text = re.sub(r'(?i)(Architecture as past history[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.436742">\\1</a>', text)
text = re.sub(r'(?i)(Family history in England ?. c[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.442361">\\1</a>', text)
text = re.sub(r'(?i)(Manufacturing the past ?. col[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.444984">\\1</a>', text)
text = re.sub(r'(?i)(Early medieval writers on fi[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.445113">\\1</a>', text)
text = re.sub(r'(?i)(Michael Drayton and early mo[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.445547">\\1</a>', text)
text = re.sub(r'(?i)(A critical edition of the li[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.447248">\\1</a>', text)
text = re.sub(r'(?i)(Evagrius Scholasticus the ch[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.447517">\\1</a>', text)
text = re.sub(r'(?i)(Chronography and Early Greek[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.448757">\\1</a>', text)
text = re.sub(r'(?i)(The Bolshevization of soviet[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.448872">\\1</a>', text)
text = re.sub(r'(?i)(An edition and translation o[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.451512">\\1</a>', text)
text = re.sub(r'(?i)(Francis Bacon ?. The study of [^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.451555">\\1</a>', text)
text = re.sub(r'(?i)(The possibility of objectivi[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.457050">\\1</a>', text)
text = re.sub(r'(?i)(The treatment of military op[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.457250">\\1</a>', text)
text = re.sub(r'(?i)(French historical novels 181[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.457416">\\1</a>', text)
text = re.sub(r'(?i)(Studies in the Lives of the [^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.458788">\\1</a>', text)
text = re.sub(r'(?i)(Idealism and the Study of Hi[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.458954">\\1</a>', text)
text = re.sub(r'(?i)(The history of the Jazira 11[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.459177">\\1</a>', text)
text = re.sub(r'(?i)(Economic Theory in Historica[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.459836">\\1</a>', text)
text = re.sub(r'(?i)(Introduction and commentary [^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.463425">\\1</a>', text)
text = re.sub(r'(?i)(The political ?. religious and[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.464870">\\1</a>', text)
text = re.sub(r'(?i)(A reconsideration of the his[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.465477">\\1</a>', text)
text = re.sub(r'(?i)(The Settlement Rationale ?. A [^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.466974">\\1</a>', text)
text = re.sub(r'(?i)(Time and the Land ?. The Work[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.468751">\\1</a>', text)
text = re.sub(r'(?i)(The life and works of Ibn Ha[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.469834">\\1</a>', text)
text = re.sub(r'(?i)(Flavius Josephus ?. Jewish Hi[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.469860">\\1</a>', text)
text = re.sub(r'(?i)(The mildrith legend ?. a stud[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.470910">\\1</a>', text)
text = re.sub(r'(?i)(British historiography on Br[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.472815">\\1</a>', text)
text = re.sub(r'(?i)(The chronographia of Michael[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.473335">\\1</a>', text)
text = re.sub(r'(?i)(Perspective and method in ea[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.474050">\\1</a>', text)
text = re.sub(r'(?i)(The social and continental b[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.474854">\\1</a>', text)
text = re.sub(r'(?i)(Aristotle.?s treatment of his[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.474953">\\1</a>', text)
text = re.sub(r'(?i)(The Growth of Working Class [^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.476079">\\1</a>', text)
text = re.sub(r'(?i)(Suetonius on the emperor ?. s[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.476352">\\1</a>', text)
text = re.sub(r'(?i)(Tuscan Historiography C 1400[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.476725">\\1</a>', text)
text = re.sub(r'(?i)(History as celebration ?. Cas[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.476896">\\1</a>', text)
text = re.sub(r'(?i)(Economic and Social Interpre[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.477555">\\1</a>', text)
text = re.sub(r'(?i)(A critical edition of the Ta[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.478570">\\1</a>', text)
text = re.sub(r'(?i)(A critical edition of Al-Ara[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.478571">\\1</a>', text)
text = re.sub(r'(?i)(Attitudes to nationality in [^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.480531">\\1</a>', text)
text = re.sub(r'(?i)(A critical edition of Al-Lu.?[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.486822">\\1</a>', text)
text = re.sub(r'(?i)(The scholar advocate ?. Rudol[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.495251">\\1</a>', text)
text = re.sub(r'(?i)(An analysis of the earliest [^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.495418">\\1</a>', text)
text = re.sub(r'(?i)(The Arab tribes from J?hil?y[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.496423">\\1</a>', text)
text = re.sub(r'(?i)(Philosophic historiography i[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.496688">\\1</a>', text)
text = re.sub(r'(?i)(Christian-Muslim relations a[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.497554">\\1</a>', text)
text = re.sub(r'(?i)(Representations of history i[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.498079">\\1</a>', text)
text = re.sub(r'(?i)(History and Legend in the Ch[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.499963">\\1</a>', text)
text = re.sub(r'(?i)(British scholarship and Musl[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.503449">\\1</a>', text)
text = re.sub(r'(?i)(The martyrology of Jean Cres[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.503562">\\1</a>', text)
text = re.sub(r'(?i)(Problems in historical const[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.504464">\\1</a>', text)
text = re.sub(r'(?i)(The culture of enthusiasm ?. [^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.504805">\\1</a>', text)
text = re.sub(r'(?i)(Outside Auschwitz ?. History ?. [^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.506085">\\1</a>', text)
text = re.sub(r'(?i)(Julius Caesar in the Early I[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.508650">\\1</a>', text)
text = re.sub(r'(?i)(The construction of Zi zhi t[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.508680">\\1</a>', text)
text = re.sub(r'(?i)(The Islamic Conquest of Spai[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.508764">\\1</a>', text)
text = re.sub(r'(?i)(Objects of Evidence ?. Coloni[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.508989">\\1</a>', text)
text = re.sub(r'(?i)(Mustafa Selaniki.?s history o[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.510055">\\1</a>', text)
text = re.sub(r'(?i)(The sword of the lord ?. West[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.511246">\\1</a>', text)
text = re.sub(r'(?i)(The history and politics of [^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.511805">\\1</a>', text)
text = re.sub(r'(?i)(English literature on the Ot[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.512876">\\1</a>', text)
text = re.sub(r'(?i)(A study of Bede.?s Historiae[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.513025">\\1</a>', text)
text = re.sub(r'(?i)(The chronicle of Alfonson II[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.513910">\\1</a>', text)
text = re.sub(r'(?i)(Rectifying the .?ignoraunce o[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.515472">\\1</a>', text)
text = re.sub(r'(?i)(Opening the Hidden Land ?. St[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.517257">\\1</a>', text)
text = re.sub(r'(?i)(Knowledge transfer in action[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.517637">\\1</a>', text)
text = re.sub(r'(?i)(Turkey and Western subjectiv[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.518237">\\1</a>', text)
text = re.sub(r'(?i)(.?Answering the calls of the [^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.518512">\\1</a>', text)
text = re.sub(r'(?i)(The Zafar-namah of Hamdallah[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.521201">\\1</a>', text)
text = re.sub(r'(?i)("The ""other"" feudalism ?. a[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.521258">\\1</a>', text)
text = re.sub(r'(?i)(Gold Coast Historian and the[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.522361">\\1</a>', text)
text = re.sub(r'(?i)(A critical edition of Kit?b [^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.523388">\\1</a>', text)
text = re.sub(r'(?i)(A critical edition of the An[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.523512">\\1</a>', text)
text = re.sub(r'(?i)(The Daily Mail Ideal Home ex[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.523852">\\1</a>', text)
text = re.sub(r'(?i)(Cosmo Innes and the sources [^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.529132">\\1</a>', text)
text = re.sub(r'(?i)(A narrative in relief ?. the [^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.530390">\\1</a>', text)
text = re.sub(r'(?i)(Crosses in circulation ?. Pro[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.533485">\\1</a>', text)
text = re.sub(r'(?i)(The archaeology and conserva[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.534916">\\1</a>', text)
text = re.sub(r'(?i)(Jan van Naaldwijk.?s chronicl[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.536786">\\1</a>', text)
text = re.sub(r'(?i)(The idea of the south in pos[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.538297">\\1</a>', text)
text = re.sub(r'(?i)(Remembering the First Crusad[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.540108">\\1</a>', text)
text = re.sub(r'(?i)(The historiography of ancien[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.542259">\\1</a>', text)
text = re.sub(r'(?i)(Traditional Thai historiogra[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.544360">\\1</a>', text)
text = re.sub(r'(?i)(Instruments of power ?. devel[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.548774">\\1</a>', text)
text = re.sub(r'(?i)(The role of history in the r[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.552002">\\1</a>', text)
text = re.sub(r'(?i)(.?The language of the naked f[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.554673">\\1</a>', text)
text = re.sub(r'(?i)(Telling people.?s histories ?.[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.554848">\\1</a>', text)
text = re.sub(r'(?i)(Enlightenment contra humanis[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.561809">\\1</a>', text)
text = re.sub(r'(?i)(Hiding behind history ?. Wins[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.570041">\\1</a>', text)
text = re.sub(r'(?i)(Towards reflexive practice ?.[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.571643">\\1</a>', text)
text = re.sub(r'(?i)(Religion in Tacitus.? Annals [^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.571658">\\1</a>', text)
text = re.sub(r'(?i)(Historiography and visual cu[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.583380">\\1</a>', text)
text = re.sub(r'(?i)(Making history ?. the role of[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.585059">\\1</a>', text)
text = re.sub(r'(?i)(The construction of national[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.587392">\\1</a>', text)
text = re.sub(r'(?i)(Real life stories in everyda[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.591043">\\1</a>', text)
text = re.sub(r'(?i)(A critical study of the Libe[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.595877">\\1</a>', text)
text = re.sub(r'(?i)(Imagining resistance ?. Briti[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.597394">\\1</a>', text)
text = re.sub(r'(?i)(Archaeological discourse at [^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.598947">\\1</a>', text)
text = re.sub(r'(?i)(Archaeology and place[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.602681">\\1</a>', text)
text = re.sub(r'(?i)(Victorian negotiations with [^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.605320">\\1</a>', text)
text = re.sub(r'(?i)(Herodotus and Hellenistic cu[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.609020">\\1</a>', text)
text = re.sub(r'(?i)(Writing history in the Third[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.611678">\\1</a>', text)
text = re.sub(r'(?i)(From archaic to classical ?. [^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.611745">\\1</a>', text)
text = re.sub(r'(?i)(A study of 15th-century Otto[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.612101">\\1</a>', text)
text = re.sub(r'(?i)(Tracing the reception of the[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.614798">\\1</a>', text)
text = re.sub(r'(?i)(Historical justification and[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.620329">\\1</a>', text)
text = re.sub(r'(?i)(Contested histories or multi[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.620462">\\1</a>', text)
text = re.sub(r'(?i)(Literary writing and the rec[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.621174">\\1</a>', text)
text = re.sub(r'(?i)(Aby Warburg and art in Hambu[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.621805">\\1</a>', text)
text = re.sub(r'(?i)(Geography in early Christian[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.621981">\\1</a>', text)
text = re.sub(r'(?i)(The construction of a large [^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.622222">\\1</a>', text)
text = re.sub(r'(?i)(Classical scholarship ?. anthr[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.625397">\\1</a>', text)
text = re.sub(r'(?i)(A new Liberal descent ?. the [^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.627573">\\1</a>', text)
text = re.sub(r'(?i)(.?X.? marks the spot ?. the his[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.628637">\\1</a>', text)
text = re.sub(r'(?i)(Increasing the digital liter[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.629645">\\1</a>', text)
text = re.sub(r'(?i)(The British .?bluesman.? ?. Pau[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.631089">\\1</a>', text)
text = re.sub(r'(?i)(Writing British national his[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.631319">\\1</a>', text)
text = re.sub(r'(?i)(Settlement and field pattern[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.634239">\\1</a>', text)
text = re.sub(r'(?i)(The Attlee governments in pe[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.645406">\\1</a>', text)
text = re.sub(r'(?i)(David Hume of Godscroft ?. hi[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.651468">\\1</a>', text)
text = re.sub(r'(?i)(The emulation of nations ?. W[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.651848">\\1</a>', text)
text = re.sub(r'(?i)(The language of character an[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.652108">\\1</a>', text)
text = re.sub(r'(?i)(Objective history and the in[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.652825">\\1</a>', text)
text = re.sub(r'(?i)(The nature of theoretical hi[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.657970">\\1</a>', text)
text = re.sub(r'(?i)(The historical works of Jon [^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.661902">\\1</a>', text)
text = re.sub(r'(?i)(The chronicle and career of [^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.662039">\\1</a>', text)
text = re.sub(r'(?i)(The development of British I[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.662653">\\1</a>', text)
text = re.sub(r'(?i)(Narratives of Protestant mis[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.663834">\\1</a>', text)
text = re.sub(r'(?i)(The Sehname-i Humayun of Ta.?[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.664004">\\1</a>', text)
text = re.sub(r'(?i)(The British debate on the Fr[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.664102">\\1</a>', text)
text = re.sub(r'(?i)(Collecting and displaying .?J[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.669978">\\1</a>', text)
text = re.sub(r'(?i)(The amateur and the professi[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.670421">\\1</a>', text)
text = re.sub(r'(?i)(The Byzantine church histori[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.670613">\\1</a>', text)
text = re.sub(r'(?i)(The apocalyptic tradition in[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.670647">\\1</a>', text)
text = re.sub(r'(?i)(Nicolaus of Damascus ?. his h[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.673999">\\1</a>', text)
text = re.sub(r'(?i)(The production of history ?. [^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.689606">\\1</a>', text)
text = re.sub(r'(?i)(Beyond the foreigner ?. repre[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.694784">\\1</a>', text)
text = re.sub(r'(?i)(.?Culture and society.? in con[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.708727">\\1</a>', text)
text = re.sub(r'(?i)(The role of the state in the[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.740870">\\1</a>', text)
text = re.sub(r'(?i)(The Works of Jehan Creton ?. A[^<]+)', '<a href="https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.757604">\\1</a>', text)
text = re.sub(r'(?i)(Binary file ethosfull.csv ma[^<]+)', '<a href="">\\1</a>', text)


f = open(finaloutfile, "w")
f.write(text)
f.close()