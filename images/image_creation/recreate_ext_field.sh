gnuplot ../external_field_at_surface.gnuplot

sed --in-place 's|\includegraphics{external_field_at_surface}|\includegraphics{perp_rec/external_field_at_surface}|' external_field_at_surface.tex

epstopdf external_field_at_surface.eps

mv external_field_at_surface.tex external_field_at_surface.pdf ../

rm external_field_at_surface.eps